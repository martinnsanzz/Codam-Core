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
    NAME = auto()
    PARAM = auto()
    END = auto()


class JSONStateMachine(BaseModel):
    current_state: Optional[GenerationState] = Field(default=GenerationState.NAME)
    llm_output: str = Field(default="")
    chosen_function: Optional[str] = Field(default="")


class Engine(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    prompts: list[Prompt]
    functions_lookup: FunctionLookup
    small_llm: Small_LLM_Model
