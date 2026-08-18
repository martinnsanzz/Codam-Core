# Built-in modules
from typing import Any, Optional, TypeAlias

# Installed modules
from pydantic import BaseModel, Field

FunctionLookup: TypeAlias = dict[str, dict[str, Any]]


class Prompt(BaseModel):
    prompt: str = Field(default="")
    name: Optional[str] = Field(default=None)
    parameters: dict[str, Any] = Field(default_factory=dict)

    def build_prompt(self, function_lookup: FunctionLookup) -> str:
        function_names = list(function_lookup.keys())

        system_content = (
            "You are a function-calling system. Given a user request, respond with "
            "exactly one JSON object in this format: "
            '{"name": "<function_name>", "parameters": {<param_name>: <value>, ...}}. '
            "Do not include any explanation, reasoning, or extra text — only the JSON object.\n\n"
            "Available functions:\n"
            f"{function_names}"
        )

        return (
            f"<|im_start|>system\n{system_content}<|im_end|>\n"
            f"<|im_start|>user\n{self.prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
