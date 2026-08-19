# Built-in modules
from pathlib import Path
from json import loads, JSONDecodeError
from typing import Any, TypeAlias

# Local modules
from .exceptions import CustomError

FunctionsList: TypeAlias = list[dict[str, Any]]
FunctionLookup: TypeAlias = dict[str, dict[str, Any]]


def load_json(json_file: Path) -> list[dict[str, Any]]:
    try:
        with open(json_file) as f:
            raw_content = f.read()
            if not raw_content:
                raise CustomError(f"File {json_file} is empty")
            content: list[dict[str, str]] = loads(raw_content)
            return content
    except FileNotFoundError as e:
        raise CustomError(f"File not found: {e}") from e
    except JSONDecodeError as e:
         raise CustomError(f"Wrong JSON format in {json_file}: {e}") from e


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