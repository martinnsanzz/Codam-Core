# Built-in modules
from typing import Any

# Local modules
from .utils import CustomError

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


def config_parser(file_name: str) -> dict[str, Any]:
    with open(file_name, "r") as file:
        content = file.readlines()
        return _extract_config_data(content)


def _extract_config_data(file_data: list[str]) -> dict[str, Any]:
    maze_config: dict[str, Any] = {}

    for line in file_data:
        if "#" not in line:
            tmp: list[str] = line.split("=")
            maze_config.update({tmp[0].upper(): (tmp[1].strip("\n"))})
    _validate_config_data(maze_config)
    return maze_config


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
