# Built-in modules
from typing import Self, Callable, Optional
from re import compile, match

# Installed modules
from pydantic import BaseModel, ConfigDict, model_validator
from llm_sdk import Small_LLM_Model
import numpy as np

# Local modules
from .states import NumState, StrState
from .prompt_class import Prompt

STRING_PATTERN  = compile(r'^"(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*"$')
NUMBER_PATTERN  = compile(r'^-?\d+\.\d+$')
INTEGER_PATTERN = compile(r'^-?\d+$')
VALID_BOOLEAN = [True, False]

MAX_DECODE_NUM = 10
MAX_DECODE_STR = 40
MAX_DECODE_BOOL = 6


class Parameter(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    prompt_obj: Prompt
    param_name: str
    param_type: str
    id_to_token: dict[int, str]
    small_llm: Optional[Small_LLM_Model]

    @model_validator(mode="after")
    def check_type(self) -> Self:
        valid_types = ["number", "integer", "string", "boolean"]

        if self.param_type not in valid_types:
            raise ValueError("Incorrect parameter type.\n"
                             f" - Supported: {valid_types}\n"
                             f" - Found: {self.param_type}")
        return self

    def get_param(self, candidates: dict[int, str],
                  system_prompt: str) -> int | float | str | bool:
        type_to_func: dict[Callable] = {
                "number": self.get_number,
                "integer": self.get_number,
                "string": self.get_string,
                "boolean": self.get_boolean,
        }

        return type_to_func[self.param_type](candidates, system_prompt)

    def get_number(self, candidates: dict[int, str], system_prompt:str) -> float:
        state = NumState.START
        accumulated = ""
        step_count = 0

        prompt = self.prompt_obj.prompt
        tokenization = self.small_llm.encode(system_prompt).tolist()[0]

        if self.param_type == "integer":
            num_in_prompt = self.extract_nums_from_prompt(prompt, "integer")
        elif self.param_type == "number":
            num_in_prompt = self.extract_nums_from_prompt(prompt, "number")

        while state != NumState.DONE:
            logits = self.small_llm.get_logits_from_input_ids(tokenization)
            np_array = np.array(logits)
            np_array[:] = -np.inf

            for token_id, candidate in candidates.items():
                total = accumulated + candidate

                if any(name.startswith(total) for name in num_in_prompt):
                    np_array[token_id] = logits[token_id]

            if np.all(np.isneginf(np_array)):
                raise TimeoutError(
                    f"No valid candidate for {self.param_name!r} "
                    f"(type={self.param_type}); accumulated={accumulated!r}"
                )

            best_id = int(np.argmax(np_array))
            best_str = self.id_to_token.get(best_id, "")
            accumulated += best_str
            tokenization.append(best_id)
            state = self.num_state(accumulated, self.prompt_obj.prompt, self.param_type)

            step_count += 1
            if step_count == MAX_DECODE_NUM:
                raise TimeoutError(
                    f"Exceeded {MAX_DECODE_NUM} steps for {self.param_name!r}; "
                    f"accumulated={accumulated!r}")

        return float(accumulated) if self.param_type == "number" else int(accumulated)

    def get_string(self, candidates: dict[int, str], prompt_text:str) -> str:
        return "Hello"

    def get_boolean(self, candidates: dict[int, str], prompt_text:str) -> bool:
        return True

    @staticmethod
    def str_state(text: str) -> StrState:
        if match(STRING_PATTERN, text):
            return StrState.CLOSED
        else:
            return StrState.OPEN

    @staticmethod
    def num_state(num: str, prompt: str, param_type: str) -> NumState:
        if not num:
            return NumState.START

        clean_prompt = prompt.rstrip(".?")

        if param_type == "integer":
            if match(INTEGER_PATTERN, num) and num in clean_prompt.split():
                return NumState.DONE
            elif match(INTEGER_PATTERN, num) and num not in clean_prompt.split():
                return NumState.INT_DIGITS
        elif param_type == "number":
            prompt_float = []

            for word in clean_prompt.split():
                try:
                    prompt_float.append(str(float(word)))
                except ValueError:
                    prompt_float.append(word)
            if match(NUMBER_PATTERN, num) and num in prompt_float:
                return NumState.DONE

        if num == "-":
            return NumState.IN_MINUS
        elif num[-1] == ".":
            return NumState.IN_DOT
        elif "." in num and num[-1].isdigit():
            return NumState.FRAC_DIGITS
        else:
            return NumState.INT_DIGITS

    def extract_nums_from_prompt(self, prompt: str, type: str) -> list[str]:
        number_pattern = compile(r'-?\d+(?:\.\d+)?')
        nums = number_pattern.findall(prompt)

        used_values = {float(v) for v in self.prompt_obj.parameters.values()
                    if isinstance(v, (int, float))}

        remaining = [n for n in nums if float(n) not in used_values]

        if type == "integer":
            return remaining
        elif type == "number":
            return [str(float(num)) for num in remaining]
        return remaining
