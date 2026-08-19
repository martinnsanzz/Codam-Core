# Built-in modules
from typing import Any, Optional
from json import dumps

# Installed modules
from pydantic import BaseModel, Field


class Prompt(BaseModel):
    prompt: str = Field(default="")
    name: Optional[str] = Field(default="")
    parameters: Optional[dict[str, Any]] = Field(default={})

    def build_prompt(self, state: str,
                     function_names: Optional[str] = "",
                     chosen_function_name: Optional[str] = "",
                     param_spec: Optional[dict[str, Any]] = None) -> str:

        system_content_func = (
            "You are a function-selection system. Given a user request, respond with "
            "only the name of the single most suitable function from the list below. "
            "Do not include any explanation, punctuation, or extra text — output only "
            "the function name exactly as written.\n\n"
            "Available functions:\n"
            f"{function_names}"
        )
        system_content_param = (
            "You are a parameter-extraction system. The user's request will be handled "
            "by the function below. Extract the correct values for each parameter from "
            "the user's request, matching the required type exactly.\n\n"
            f"Function: {chosen_function_name}\n"
            f"Parameters required: {param_spec}\n\n"
            "Do not include any explanation, reasoning, or extra text — output only the "
            "parameter values."
        )
        system_content = system_content_func if state == "func" else system_content_param

        return (
            f"<|im_start|>system\n{system_content}<|im_end|>\n"
            f"<|im_start|>user\n{self.prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )

    def get_output(self) -> str:
        prompt_str = f'"prompt": {dumps(self.prompt)}, '
        func_str = f'"name": {dumps(self.name)}, '
        param_str = f'"parameters": {dumps(self.parameters)}'

        return "{" + prompt_str + func_str + param_str + "}"
