# Built-in modules
from typing import Any

# Installed modules
from pydantic import BaseModel, Field

# Local modules
from ..exceptions import CustomError

class Prompt(BaseModel):
    prompt: str = Field(default="")
    # future fields: name, parameters, etc.

    @staticmethod
    def from_json(prompt_json: list[dict[str, Any]]) -> list["Prompt"]:
        if not prompt_json:
            raise CustomError("No prompt found. Add a prompt to '.json file'")

        prompts: list[Prompt] = []
        for entry in prompt_json:
            if not entry.get("prompt"):
                raise CustomError("Empty prompt found, fix this !!")
            prompts.append(Prompt(prompt=entry["prompt"]))

        return prompts
