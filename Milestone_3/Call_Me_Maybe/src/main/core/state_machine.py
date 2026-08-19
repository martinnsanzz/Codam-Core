# Built-in modules
from enum import Enum, auto
from typing import Optional
from json import loads
from re import compile, Pattern, match
import time

# Installed modules
from pydantic import BaseModel, Field, ConfigDict
import numpy as np

# Local modules
from llm_sdk import Small_LLM_Model
from .loader import FunctionLookup
from .exceptions import CustomError
from ..classes import Prompt


VALID_FUNC_CHARS = compile(r'^[a-z0-9_]+$')
VALID_NUM_CHARS = compile(r'^-?\d*\.?\d*$')
VALID_STR_CHARS = compile(r'^[\x20-\x7e]+$')

STRING_PATTERN = compile(r'^"(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*"$')
NUMBER_PATTERN = compile(r'^-?\d+(\.\d+)?$')


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
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    prompts: list[Prompt]
    functions_lookup: FunctionLookup
    small_llm: Small_LLM_Model

    def prompt_loop(self) -> list[str]:
        """Resolve each prompt's function name and parameters via decoding.

        Loads the model's vocabulary once, then for every prompt drives
        a ``StateMachine`` through ``FUNC`` -> ``PARAM`` -> ``END``,
        calling ``llm_get_function``/``llm_get_param`` at each stage.

        Returns:
            list[str]: The rendered output of every prompt, in order.
        """
        llm_output = []

        vocab_path = self.small_llm.get_path_to_vocab_file()

        with open(vocab_path, 'r') as f:
            vocab_dict: dict[str, int] = loads(f.read())

        id_to_token = {token_id: token_str for token_str, token_id in vocab_dict.items()}

        i = 0
        for prompt_obj in self.prompts:
            state_machine = StateMachine(prompt=prompt_obj)

            while state_machine.current_state != GenerationState.END:
                if state_machine.current_state == GenerationState.FUNC:
                    start = time.time()
                    self.llm_get_function(id_to_token, prompt_obj)
                    end = time.time()
                    print(f"Total function time: {end - start}")
                elif state_machine.current_state == GenerationState.PARAM:
                    self.llm_get_param(id_to_token, prompt_obj)
                state_machine.get_state()
            llm_output.append(prompt_obj.get_output())
            i += 1
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

        prompt_text = prompt_obj.build_prompt(
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
        # prompt_obj.parameters = {"a": "h", "b": "f"}
        function_param = self.functions_lookup[prompt_obj.name]["parameters"]

        for param_name, param_info in function_param.items():
            param_type = param_info["type"]
    
            prompt_text = prompt_obj.build_prompt(
                "param",
                chosen_function_name=prompt_obj.name,
                param_spec=f"{param_name}: {param_type}",
            )

            candidates = self.filter_id_to_token(id_to_token, param_type)
            print(candidates)
            quit()
            tokenization = self.small_llm.encode(prompt_text).tolist()[0]
            accumulated = '"' if param_type == "string" else ""

            while True:
                logits = self.small_llm.get_logits_from_input_ids(tokenization)
                np_array = np.array(logits)
                np_array[:] = -np.inf

                for token_id in candidates.keys():
                        np_array[token_id] = logits[token_id]

                best_id = int(np.argmax(np_array))
                best_str = id_to_token.get(best_id, "")
                print(best_str)

                accumulated += best_str
                tokenization.append(best_id)

                full_regex = NUMBER_PATTERN if param_type == "number" else STRING_PATTERN
                is_complete = match(full_regex, accumulated)

                if param_type == "number":
                    is_complete = is_complete and any(c.isdigit() for c in accumulated)

                if is_complete:
                    value = accumulated.strip('"') if param_type == "string" else accumulated
                    prompt_obj.parameters[param_name] = value
                    break

    def filter_id_to_token(self, id_to_token: dict[int, str],
                           type: str) -> dict[int, str]:
        """Keep only vocabulary entries whose token string matches a pattern.

        Args:
            id_to_token: Mapping from vocabulary token ID to token string.
            pattern: Compiled regex.

        Returns:
            dict[int, str]: Subset of ``id_to_token`` whose values are
            non-empty and match ``pattern``.
        """
        pattern = VALID_NUM_CHARS if type == "number" else VALID_STR_CHARS

        filtered = {}

        for token_id, token_str in id_to_token.items():
            if token_str and pattern.match(token_str):
                filtered.update({token_id: token_str})

        return filtered

    @staticmethod
    def check_regex(value: str) -> Pattern[str]:
        accepted_values = ["string", "number"]

        match value:
            case "string":
                return compile(STRING_PATTERN)
            case "number":
                return compile(NUMBER_PATTERN)
            case _:
                raise CustomError(f"Invalid value. Accepted values {accepted_values}")