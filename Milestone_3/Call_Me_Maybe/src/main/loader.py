# Built-in modules
from pathlib import Path
from json import loads, JSONDecodeError
from typing import Any

# Local modules
from .exceptions import CustomError


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
