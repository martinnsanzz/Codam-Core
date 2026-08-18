# Built-in modules
from enum import Enum, auto
from typing import Optional, Any

# Installed modules
from pydantic import BaseModel, Field, ConfigDict

# Local modules
from llm_sdk import Small_LLM_Model
from ..classes import Prompt
from .schema import FunctionLookup


class GenerationState(Enum):
    FUNC = auto()
    PARAM = auto()
    END = auto()


class JSONStateMachine(BaseModel):
    current_state: Optional[GenerationState] = Field(default=GenerationState.FUNC)
    llm_output: str = Field(default="")
    chosen_function: Optional[str] = Field(default="")

    def get_state(prompt: Prompt) -> GenerationState:
        if not prompt.name:
            return GenerationState.FUNC
        elif not prompt.parameters:
            return GenerationState.PARAM
        else:
            return GenerationState.END


class Engine(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    prompts: list[Prompt]
    functions_lookup: FunctionLookup
    small_llm: Small_LLM_Model

    def test(self) -> str:
        llm_output = []
        prompt_1 = self.prompts[0]
        prompt_1.name = "fn_add_numbers"
        prompt_1.parameters = {"a": 2.0, "b": 3.0}

        llm_output.append(prompt_1.get_output(self.functions_lookup))

        prompt_2 = self.prompts[1]
        prompt_2.name = "fn_reverse_string"
        prompt_2.parameters = {"s": "hello"}

        llm_output.append(prompt_2.get_output(self.functions_lookup))
        return llm_output