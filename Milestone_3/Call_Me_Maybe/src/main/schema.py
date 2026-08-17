# Built-in modules
from typing import Pattern, TypeAlias, Any
from re import compile

# Local Modules
from .exceptions import CustomError

FunctionsList: TypeAlias = list[dict[str, Any]]
FunctionLookup: TypeAlias = dict[str, dict[str, Any]]


STRING_PATTERN = r'^"(?:[^"\\\x00-\x1f]|\\[nrtbf"\\/]|\\u[0-9a-fA-F]{4})*"$'
NUMBER_PATTERN = r'^-?\d+(\.\d+)?([eE][+-]?\d+)?$'


def build_function_lookup(functions_json: FunctionsList) -> FunctionLookup:
    function_lookup = {func["name"]: func for func in functions_json}

    return validate_functions(function_lookup)


def validate_functions(functions_lookup: FunctionLookup) -> FunctionLookup:
    accepted_types = ["string", "number"]

    for item in functions_lookup:
        for param in functions_lookup[item]["parameters"]:
            var_type = functions_lookup[item]["parameters"][param]["type"]
            if var_type not in accepted_types:
                raise CustomError(f"Wrong parameter type: '{var_type}'."
                                  f" Accepted types {accepted_types}")
        if functions_lookup[item]["returns"]["type"] not in accepted_types:
            raise CustomError(f"Wrong return type: '{var_type}'."
                              f" Accepted types {accepted_types}")
    return functions_lookup


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