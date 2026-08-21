# Built-in modules
from enum import Enum, auto
from typing import Optional, Any
from json import loads
import time
from re import compile

# Installed modules
from pydantic import BaseModel, Field, ConfigDict
import numpy as np

# Local modules
from llm_sdk import Small_LLM_Model
from .loader import FunctionLookup
from .exceptions import GenerationTimeoutError, CustomError
from ..classes import Prompt
from ..visual import display_title, display_prompt_info, display_total_info


VALID_FUNC_CHARS    = compile(r'^[a-z0-9_]+$')
VALID_NUM_CHARS     = compile(r'^-?\d*\.?\d*$')
VALID_STR_CHARS     = compile(r'^[\x20-\x7e]+$')

STRING_PATTERN      = compile(r'^(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*$')
NUMBER_PATTERN      = compile(r'^-?\d+(\.\d+)?$')

QUOTED_PHRASE       = compile(r'["\']([^"\']*)["\']')
DBL_QUOTED_PHRASE   = compile(r'"([^"]*)"')
SGL_QUOTED_PHRASE   = compile(r"'([^']*)'")

MAX_DECODE_STEPS    = 20


class GenerationState(Enum):
    """Represent states of a generation/parsing state machine.

    Attributes:
        FUNC: State for identifying or processing the function/conversion.
        PARAM: State for processing parameters/arguments.
        END: Terminal state indicating parsing is complete.
    """
    FUNC = auto()
    PARAM = auto()
    END = auto()


class StateMachine(BaseModel):
    """Track generation state based on prompt completeness.

    Attributes:
        prompt: The prompt being evaluated to determine progress.
        current_state: The current phase of generation. Defaults to
            ``GenerationState.FUNC``.
    """
    prompt: Prompt
    current_state: Optional[GenerationState] = Field(default=GenerationState.FUNC)

    def get_state(self) -> None:
        """Update ``current_state`` based on the prompt's completeness.

        Notes:
            Progresses through ``FUNC`` -> ``PARAM`` -> ``END`` as
            ``prompt.name`` and ``prompt.parameters`` become populated.
        """
        if not self.prompt.name:
            self.current_state = GenerationState.FUNC
        elif not self.prompt.parameters:
            self.current_state = GenerationState.PARAM
        else:
            self.current_state = GenerationState.END


class Engine(BaseModel):
    """Drive constrained token-by-token generation to fill prompts.

    Uses a small local LLM plus a state machine per prompt to
    generate a function name and its parameters via logit masking,
    then collects each prompt's rendered output.

    Attributes:
        prompts: The prompts to process into filled function calls.
        functions_lookup: Mapping of known function names to their
            parameter specifications.
        small_llm: The local model used for constrained decoding.
        id_to_token: Object containg all vocab from llm in {int: str} 
            format
        visual_mode: Boolean based on flag to display visual on cli
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    prompts: list[Prompt]
    functions_lookup: FunctionLookup
    small_llm: Small_LLM_Model
    id_to_token: dict[int, str] = Field(default_factory=dict)
    visual_mode: bool

    def model_post_init(self, context: Any) -> None:
        """Load the model's vocabulary and build the id-to-token map.

        Runs automatically after Pydantic validation/construction.
        Optionally displays a title banner, then reads the small
        LLM's vocab file (a JSON object mapping token string to
        token ID) and inverts it into ``self.id_to_token``.
        """
        super().model_post_init(context)
        if self.visual_mode:
            display_title()

        vocab_path = self.small_llm.get_path_to_vocab_file()
        with open(vocab_path, 'r') as f:
            vocab_dict: dict[str, int] = loads(f.read())

        self.id_to_token = {token_id: token_str for token_str,
                            token_id in vocab_dict.items()}

        self.id_to_token = {
            token_id: token_str.replace('\u0120', ' ')
            for token_str, token_id in vocab_dict.items()
        }

    def prompt_loop(self) -> list[str]:
        """Resolve each prompt's function name and parameters via decoding.

        For every prompt drives a ``StateMachine`` through 
        ``FUNC`` -> ``PARAM`` -> ``END``, calling 
        ``llm_get_function``/``llm_get_param`` at each stage.

        Returns:
            list[str]: The rendered output of every prompt, in order.
        """
        llm_output = []
        i = 0
        error_log = 0
        total_time = 0
        for prompt_obj in self.prompts:
            error_msg = ""
            start = time.time()
            state_machine = StateMachine(prompt=prompt_obj)
            try:
                if not prompt_obj.prompt:
                    raise CustomError(f"Prompt {i} is empty !!")
                while state_machine.current_state != GenerationState.END:
                    if state_machine.current_state == GenerationState.FUNC:
                        self.llm_get_function(self.id_to_token, prompt_obj)
                    elif state_machine.current_state == GenerationState.PARAM:
                        self.llm_get_param(self.id_to_token, prompt_obj)
                    state_machine.get_state()
            except (GenerationTimeoutError, CustomError)as e:
                error_log += 1
                error_msg = e
            llm_output.append(prompt_obj.get_output())
            end = time.time()
            prompt_time = end - start
            total_time += prompt_time
            if self.visual_mode:
                display_prompt_info(prompt_obj, i, error_msg, prompt_time)
            i += 1
        if self.visual_mode:
            display_total_info(error_log, len(self.prompts), total_time)
        return llm_output

    def llm_get_function(self, id_to_token: dict[int, str],
                         prompt_obj: Prompt) -> None:
        """Decode tokens until a valid function name is assembled.

        Repeatedly masks the model's logits to only the token IDs whose
        string is a valid name character and whose accumulated text is
        a prefix of a known function name, picks the highest-scoring 
        allowed token, and appends it. Sets ``prompt_obj.name`` once the 
        accumulated text exactly matches an entry in ``functions_lookup``.

        Args:
            id_to_token: Mapping from vocabulary token ID to token string.
            prompt_obj: The prompt whose ``name`` field is populated
                in place once decoding completes.
        """
        function_names = list(self.functions_lookup.keys())

        tokenize_funcs = self.small_llm.encode(''.join(function_names)).tolist()[0]
        candidates = {id: str for id, str in id_to_token.items() if id in tokenize_funcs}

        prompt_text = prompt_obj.sys_prompt(
            "func",
            function_names='|'.join(function_names)
        )

        tokenization = self.small_llm.encode(prompt_text).tolist()[0]
        accumulated = ""

        while not prompt_obj.name:
            logits = self.small_llm.get_logits_from_input_ids(tokenization)
            np_array = np.array(logits)
            np_array[:] = -np.inf

            for token_id, candidate in candidates.items():
                total = accumulated + candidate
                if any(name.startswith(total) for name in function_names):
                    np_array[token_id] = logits[token_id]

            best_id = int(np.argmax(np_array))
            best_str = id_to_token.get(best_id, "")

            accumulated += best_str
            tokenization.append(best_id)

            if accumulated in function_names:
                prompt_obj.name = accumulated


    def llm_get_param(self, id_to_token: dict[int, str],
                      prompt_obj: Prompt) -> None:
        function_param = self.functions_lookup[prompt_obj.name]["parameters"]
        words_prompt = self.divide_prompt(prompt_obj.prompt)

        for param_name, param_info in function_param.items():
            param_type = param_info["type"]
            candidates = self.filter_id_to_token(id_to_token, param_type)
    
            prompt_text = prompt_obj.sys_prompt(
                "param",
                fn_description=self.functions_lookup[prompt_obj.name]["description"],
                param_spec=f"{param_name}: {param_type}",
            )

            tokenization = self.small_llm.encode(prompt_text).tolist()[0]
            accumulated = ""
            
            for i in range(MAX_DECODE_STEPS):
                logits = self.small_llm.get_logits_from_input_ids(tokenization)
                np_array = np.array(logits)
                np_array[:] = -np.inf

                for token_id, candidate in candidates.items():
                    total = accumulated + candidate
                    if any(name.startswith("'") for name in words_prompt) and \
                        not accumulated.startswith("'") and candidate == "'":
                        np_array[token_id] = np.inf
                        break
                    elif any(name.startswith('"') for name in words_prompt) and \
                        not accumulated.startswith('"') and candidate == '"':
                        np_array[token_id] = np.inf
                        break
                    elif any(name.startswith(total) for name in words_prompt):
                        np_array[token_id] = logits[token_id]

                if np.all(np.isneginf(np_array)):
                    raise GenerationTimeoutError(
                        f"No valid candidate for {param_name!r} "
                        f"(type={param_type}); accumulated={accumulated!r}"
                    )

                best_id = int(np.argmax(np_array))
                best_str = id_to_token.get(best_id, "")

                accumulated += best_str
                tokenization.append(best_id)

                if accumulated in words_prompt:
                    words_prompt.remove(accumulated)
                    prompt_obj.parameters[param_name] = accumulated.strip('"\'')
                    break
            else:
                raise GenerationTimeoutError(
                    f"Exceeded {MAX_DECODE_STEPS} steps for {param_name!r}; "
                    f"accumulated={accumulated!r}, words_prompt={words_prompt!r}"
                )

    def filter_id_to_token(self, id_to_token: dict[int, str],
                           type: str) -> dict[int, str]:
        """Keep only vocabulary entries whose token string matches a pattern."""
        pattern = VALID_NUM_CHARS if type == "number" else VALID_STR_CHARS

        filtered = {}

        for token_id, token_str in id_to_token.items():
            if token_str and pattern.match(token_str):
                filtered.update({token_id: token_str})

        return filtered

    @staticmethod
    def divide_prompt(prompt: str) -> list[str]:
        if '"' in prompt or "'" in prompt:
            after_dbl = DBL_QUOTED_PHRASE.sub("", prompt)
            remaining = SGL_QUOTED_PHRASE.sub("", after_dbl).split()

            words_in_prompt = (
                [f'"{q}"' for q in DBL_QUOTED_PHRASE.findall(prompt)]
                + [f"'{q}'" for q in SGL_QUOTED_PHRASE.findall(after_dbl)]
                + remaining
            )
        else:
            words_in_prompt = prompt.split()

        words = []
        for word in words_in_prompt:
            try:
                words.append(str(float(word)))
            except ValueError:
                words.append(word)
        return words
