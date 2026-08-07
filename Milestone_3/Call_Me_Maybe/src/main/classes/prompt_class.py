# Built-in Modules
from pathlib import Path
from pydantic import BaseModel, Field


class Prompt(BaseModel):
    prompt: str = Field(default="")
