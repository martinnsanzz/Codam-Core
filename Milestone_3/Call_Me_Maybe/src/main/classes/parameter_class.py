# Built-in modules
from typing import Self, Callable, Optional
from re import compile, match

# Installed modules
from pydantic import BaseModel, ConfigDict, model_validator
from llm_sdk import Small_LLM_Model
import numpy as np

# Local modules
from .states import NumState, StrState, get_num_state
from .prompt_class import Prompt

VALID_BOOLEAN = ["true", "false"]

MAX_DECODE_NUM = 15
MAX_DECODE_STR = 40
MAX_DECODE_BOOL = 6


class Parameter(BaseModel):
    """Extract a single typed parameter value via constrained LLM decoding.

    Wraps a `Prompt` and a `Small_LLM_Model` instance to decode one
    parameter of a given `param_type` token-by-token, masking the model's
    logits at each step so only candidates consistent with the source
    prompt can be selected.

    Attributes:
        prompt_obj: The `Prompt` instance holding the source prompt text
            and any already-resolved parameter values.
        param_name: Name of the parameter being extracted.
        param_type: One of "number", "integer", "string", or "boolean".
        id_to_token: Mapping from vocabulary token id to its string form.
        small_llm: The local model SDK instance used for encoding and
            logit generation, or ``None`` if not yet attached.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    prompt_obj: Prompt
    param_name: str
    param_type: str
    id_to_token: dict[int, str]
    small_llm: Optional[Small_LLM_Model]

    @model_validator(mode="after")
    def check_type(self) -> Self:
        """Validate that `param_type` is one of the supported types.

        Returns:
            Self: The validated model instance, unchanged.

        Raises:
            ValueError: If `param_type` is not one of "number", "integer",
                "string", or "boolean".
        """
        valid_types = ["number", "integer", "string", "boolean"]

        if self.param_type not in valid_types:
            raise ValueError("Incorrect parameter type.\n"
                             f" - Supported: {valid_types}\n"
                             f" - Found: {self.param_type}")
        return self

    def get_param(self, candidates: dict[int, str],
                  system_prompt: str) -> int | float | str | bool:
        """Dispatch parameter extraction to the type-specific decoder.

        Args:
            candidates: Mapping from candidate next-token id to its string
                form, as offered by the decoder for the current step.
            system_prompt: The system prompt text supplied to the LLM for
                this decoding step.

        Returns:
            int | float | str | bool: The decoded value, typed according
            to `self.param_type`.
        """
        type_to_func: dict[Callable] = {
                "number": self.get_number,
                "integer": self.get_number,
                "string": self.get_string,
                "boolean": self.get_boolean,
        }

        return type_to_func[self.param_type](candidates, system_prompt)

    def get_number(self, candidates: dict[int, str], system_prompt:str) -> float | int:
        """Decode a numeric parameter token-by-token with logit masking.

        At each step, masks out every candidate token whose accumulation
        onto the current partial value is not a prefix of some number
        found in `self.prompt_obj.prompt`, then greedily selects the
        highest-logit remaining candidate. Decoding stops when the
        accumulated string reaches `NumState.DONE`.

        Args:
            candidates: Mapping from candidate next-token id to its string
                form, as offered by the decoder for the current step.
            system_prompt: Text encoded via `self.small_llm.encode` to seed
                the token-id sequence passed to `get_logits_from_input_ids`.

        Returns:
            float: The decoded value as a ``float`` when `self.param_type`
            is "number" or an ``int`` when `self.param_type` is "integer",

        Raises:
            RuntimeError: If no candidate token keeps `accumulated`
                consistent with any number extracted from the prompt.
            TimeoutError: If decoding exceeds `MAX_DECODE_NUM` steps.
        """
        state = NumState.START
        accumulated = ""
        step_count = 0

        prompt = self.prompt_obj.prompt
        tokenization = self.small_llm.encode(system_prompt).tolist()[0]

        num_in_prompt = self.extract_nums_from_prompt(prompt, self.param_type)

        while state != NumState.DONE:
            logits = self.small_llm.get_logits_from_input_ids(tokenization)
            np_array = np.array(logits)
            np_array[:] = -np.inf

            for token_id, candidate in candidates.items():
                total = accumulated + candidate
                if any(name.startswith(total) for name in num_in_prompt):
                    np_array[token_id] = logits[token_id]

            if np.all(np.isneginf(np_array)):
                raise RuntimeError(
                    f"No valid candidate for {self.param_name!r} "
                    f"(type={self.param_type}); accumulated={accumulated!r}"
                )

            best_id = int(np.argmax(np_array))
            best_str = self.id_to_token.get(best_id, "")
            accumulated += best_str

            tokenization.append(best_id)

            state = get_num_state(accumulated, prompt, self.param_type)

            step_count += 1
            if step_count == MAX_DECODE_NUM:
                raise TimeoutError(
                    f"Exceeded {MAX_DECODE_NUM} steps for {self.param_name!r}; "
                    f"accumulated={accumulated!r}")
    
        return float(accumulated) if self.param_type == "number" else int(accumulated)

    def get_string(self, candidates: dict[int, str], prompt_text:str) -> str:
        
        return "Hello"

    def get_boolean(self, candidates: dict[int, str], system_prompt:str) -> bool:
        """Decode a boolean parameter token-by-token with logit masking.

        At each step, masks out every candidate token whose accumulation
        onto the current partial value is not a prefix of ``True`` or
        ``False``, then greedily selects the highest-logit remaining
        candidate. Decoding stops once `accumulated` matches an entry in
        `VALID_BOOLEAN`.

        Args:
            candidates: Mapping from candidate next-token id to its string
                form, as offered by the decoder for the current step.
            system_prompt: Text encoded via `self.small_llm.encode` to seed
                the token-id sequence passed to `get_logits_from_input_ids`.

        Returns:
            bool: The decoded boolean value.

        Raises:
            RuntimeError: If no candidate token keeps `accumulated`
                consistent with either boolean literal.
            TimeoutError: If decoding exceeds `MAX_DECODE_BOOL` steps.
        """
        accumulated = ""
        step_count = 0

        tokenization = self.small_llm.encode(system_prompt).tolist()[0]

        while accumulated not in VALID_BOOLEAN:
            logits = self.small_llm.get_logits_from_input_ids(tokenization)
            np_array = np.array(logits)
            np_array[:] = -np.inf

            for token_id, candidate in candidates.items():
                total = accumulated + candidate
                if any(valid.startswith(total) for valid in VALID_BOOLEAN):
                    np_array[token_id] = logits[token_id]

            if np.all(np.isneginf(np_array)):
                raise RuntimeError(
                    f"No valid candidate for {self.param_name!r} "
                    f"(type={self.param_type}); accumulated={accumulated!r}"
                )

            best_id = int(np.argmax(np_array))
            best_str = self.id_to_token.get(best_id, "")
            accumulated += best_str

            tokenization.append(best_id)

            step_count += 1
            if step_count == MAX_DECODE_BOOL:
                raise TimeoutError(
                    f"Exceeded {MAX_DECODE_NUM} steps for {self.param_name!r}; "
                    f"accumulated={accumulated!r}")
    
        return bool(accumulated)

    def extract_nums_from_prompt(self, prompt: str, param_type: str) -> list[str]:
        """Extract candidate numeric substrings from a prompt.

        Finds all integer/decimal substrings in `prompt`, excludes values
        already consumed by other resolved parameters in
        `self.prompt_obj.parameters`, and filters the remainder by
        `param_type`: for "integer", only whole numbers are kept; for
        "number", decimal-point numbers are preferred over whole numbers
        when both are present.

        Args:
            prompt: The source prompt text to scan for numbers.
            param_type: Either "integer" or "number"; determines the
                filtering rule applied to the extracted numbers.

        Returns:
            list[str]: For "integer", the remaining whole-number strings
            with no decimal point. For "number", the remaining decimal
            strings if any exist, otherwise the remaining whole numbers
            deduplicated and normalized via `float()`/`str()`.
        """
        parameters = self.prompt_obj.parameters
        number_pattern = compile(r'-?\d+(?:\.\d+)?')
        nums = number_pattern.findall(prompt)

        used_values = {float(v) for v in parameters.values()
                    if isinstance(v, (int, float))}

        remaining = [n for n in nums if float(n) not in used_values]

        if param_type == "integer":
            # Integers can only come from numbers with no decimal point
            return [n for n in remaining if "." not in n]

        decimals = [n for n in remaining if "." in n]
        whole = [n for n in remaining if "." not in n]

        if decimals and param_type == "number":
            return decimals
        return list({str(float(n)) for n in whole})
