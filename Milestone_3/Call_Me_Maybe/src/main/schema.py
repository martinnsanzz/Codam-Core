# Built-in modules
from typing import Pattern
from re import compile

# Local Modules
from .utils import CustomError

STRING_PATTERN = r'^"(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*"$'
NUMBER_PATTERN = r'^-?\d+(\.\d+)?([eE][+-]?\d+)?$'

def check_regex(value: str) -> Pattern[str]:
    accepted_values = ["string", "number"]

    match value:
        case "string":
            return compile(STRING_PATTERN)
        case "number":
            return compile(NUMBER_PATTERN)
        case _:
            raise CustomError(f"Invalid value. Accepted values {accepted_values}")


def partial_regex_validation():
    pass

def full_regex_validation():
    pass