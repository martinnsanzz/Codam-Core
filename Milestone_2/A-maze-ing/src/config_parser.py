"""
Configuration file parser with schema validation.

Reads maze configuration from a text file (key=value format with # comments),
validates all entries against a defined schema, and returns a typed dictionary.
"""

# Built-in modules
from typing import Any

# Local modules
from .utils import CustomError


# Schema: maps config key names to their expected Python types.
# Used by _validate_config_data to enforce type conversion and validation.
CONFIG_SCHEMA = {
    "WIDTH": int,
    "HEIGHT": int,
    "ENTRY": tuple,
    "EXIT": tuple,
    "OUTPUT_FILE": str,
    "PERFECT": bool,
    "SEED": int,
    "ALGHORITHM": int,
    "DISPLAY_MODE": int,
}


# Load and parse a configuration file into a typed dictionary.

# Reads a key=value format file, skips comment lines (containing "#"),
# and validates all entries against CONFIG_SCHEMA.

# Returns:
#     dict[str, Any]: Validated config dict with typed values.
#                     Keys are uppercase; values are int, tuple, bool, or str.

# Raises:
#     FileNotFoundError: If file_name does not exist.
#     CustomError: If any config key/value fails validation or type conversion.
def config_parser(file_name: str) -> dict[str, Any]:
    with open(file_name, "r") as file:
        content = file.readlines()
        return _extract_config_data(content)


# Extract key=value pairs from config file lines, skipping comments.
# Splits each non-comment line on "=" and builds a raw dict. Then validates
# all keys/values against CONFIG_SCHEMA and performs type conversion.
def _extract_config_data(file_data: list[str]) -> dict[str, Any]:
    maze_config: dict[str, Any] = {}

    for line in file_data:
        if "#" not in line:
            tmp: list[str] = line.split("=")
            maze_config.update({tmp[0].upper(): (tmp[1].strip("\n"))})
    _validate_config_data(maze_config)
    return maze_config


# Validate and type-convert config values in-place according to CONFIG_SCHEMA.
def _validate_config_data(data: dict[str, Any]) -> None:
    for key, value in data.items():
        try:
            if CONFIG_SCHEMA[key] == int:
                data[key] = int(value)
            if CONFIG_SCHEMA[key] == tuple:
                data[key] = tuple(map(int, data[key].split(",")))
            if CONFIG_SCHEMA[key] == bool:
                if value == "True":
                    data[key] = True
                elif value == "False":
                    data[key] = False
                else:
                    raise ValueError
        except ValueError:
            raise CustomError(f"Config file error: \
Invalid value for '{key}': '{value}'.")
