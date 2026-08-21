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
from ..classes import Prompt
from ..visual import display_title, display_prompt_info


VALID_FUNC_CHARS = compile(r'^[a-z0-9_]+$')
VALID_NUM_CHARS = compile(r'^-?\d*\.?\d*$')
VALID_STR_CHARS = compile(r'^[\x20-\x7e]+$')

STRING_PATTERN = compile(r'^(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*$')
NUMBER_PATTERN = compile(r'^-?\d+(\.\d+)?$')

QUOTED_PHRASE = compile(r'["\']([^"\']*)["\']')
DBL_QUOTED_PHRASE = compile(r'"([^"]*)"')
SGL_QUOTED_PHRASE = compile(r"'([^']*)'")


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
        for prompt_obj in self.prompts:
            start = time.time()
            state_machine = StateMachine(prompt=prompt_obj)
            while state_machine.current_state != GenerationState.END:
                if state_machine.current_state == GenerationState.FUNC:
                    self.llm_get_function(self.id_to_token, prompt_obj)
                elif state_machine.current_state == GenerationState.PARAM:
                    self.llm_get_param(self.id_to_token, prompt_obj)
                state_machine.get_state()
            llm_output.append(prompt_obj.get_output())
            i += 1
            end = time.time()
            total_time = end - start
            if self.visual_mode:
                display_prompt_info(prompt_obj, i, total_time)
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
        """Extract every parameter value for the prompt's chosen function.

        Splits ``prompt_obj.prompt`` into candidate words/phrases via
        ``divide_prompt``, then for each parameter declared on the
        already-selected function, builds a param-extraction prompt
        and decodes its value with ``get_param``, storing the result
        in ``prompt_obj.parameters`` in place.

        Args:
            id_to_token: Mapping from vocabulary token ID to token string.
            prompt_obj: The prompt whose ``name`` has already been set
                and whose ``parameters`` field is populated in place.
        """
        function_param = self.functions_lookup[prompt_obj.name]["parameters"]
        words_prompt = self.divide_prompt(prompt_obj.prompt)

        for param_name, param_info in function_param.items():
            param_type = param_info["type"]
    
            prompt_text = prompt_obj.sys_prompt(
                "param",
                fn_description=self.functions_lookup[prompt_obj.name]["description"],
                param_spec=f"{param_name}: {param_type}",
            )

            prompt_obj.parameters[param_name] = self.get_param(param_type, id_to_token, words_prompt, prompt_text)
        


    def get_param(self, param_type: str, id_to_token: dict[int, str],
                      words_prompt: list[str], prompt_text: str) -> str:
        """Decode tokens until a value from ``words_prompt`` is matched.

        Masks logits to tokens matching the character class for
        ``param_type`` (see ``filter_id_to_token``) whose accumulated
        text is a prefix of some entry in ``words_prompt``, picks the
        highest-scoring allowed token each step, and appends it. Stops
        once the accumulated text exactly matches one of the candidate
        words, removing that word from ``words_prompt`` so it isn't
        matched again for a later parameter.

        Args:
            param_type (str): Declared parameter type (e.g.
                ``"number"`` or ``"string"``); passed through to
                ``filter_id_to_token`` to select the allowed character
                class.
            id_to_token: Mapping from vocabulary token ID to token string.
            words_prompt: Candidate words/phrases extracted from the
                original prompt text, mutated in place (the matched
                entry is removed).
            prompt_text: The chat-formatted parameter-extraction prompt
                to condition generation on.

        Returns:
            str: The matched value, with any wrapping ``"`` or ``'``
                characters stripped.
        """
        candidates = self.filter_id_to_token(id_to_token, param_type)
        tokenization = self.small_llm.encode(prompt_text).tolist()[0]
        accumulated = ""
        print(words_prompt)
        while True:
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
                    print("Inside")
                    np_array[token_id] = np.inf
                    break
                elif any(name.startswith(total) for name in words_prompt):
                    # print(f"Token_id {token_id} -> Candidate: {candidate} -> Logits: {logits[token_id]}")
                    np_array[token_id] = logits[token_id]
            
            best_id = int(np.argmax(np_array))
            best_str = id_to_token.get(best_id, "")

            accumulated += best_str
            tokenization.append(best_id)

            if accumulated in words_prompt:
                words_prompt.remove(accumulated)
                return accumulated.strip('"\'')

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
        """Split a prompt into candidate parameter words/phrases.

        If the prompt contains no quote characters, it is simply
        whitespace-split. Otherwise, double-quoted and single-quoted
        substrings are extracted first (re-wrapped in their quote
        characters), followed by the remaining unquoted text (with all
        quoted spans removed) whitespace-split.

        Args:
            prompt (str): The raw user prompt text to divide.

        Returns:
            list[str]: Candidate words/phrases, quoted phrases included
                with their surrounding quote characters intact.
        """
        if '"' in prompt or "'" in prompt:
            words_in_prompt = []

            dbl_extracted = DBL_QUOTED_PHRASE.findall(prompt)
            after_dbl = DBL_QUOTED_PHRASE.sub("", prompt)

            sing_extracted = SGL_QUOTED_PHRASE.findall(after_dbl)
            remaining = SGL_QUOTED_PHRASE.sub("", after_dbl).split()

            if dbl_extracted:
                for quote in dbl_extracted:
                    words_in_prompt.append('"' + quote + '"')

            if sing_extracted:
                for quote in sing_extracted:
                    words_in_prompt.append("'" + quote + "'")

            for word in remaining:
                words_in_prompt.append(word)

            return words_in_prompt

            # for quote in dbl_extracted:
            #     words_in_prompt.append('"' + quote + '"')
            # for quote in sing_extracted:
            #     words_in_prompt.append("'" + quote + "'")

            return words_in_prompt
        return prompt.split()
