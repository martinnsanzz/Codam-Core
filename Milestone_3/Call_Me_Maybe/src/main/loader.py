# Built-in modules
from pathlib import Path
from json import loads, JSONDecodeError

# Local modules
from .utils import CustomError

def load_json(json_file: Path) -> list[dict[str, str]]:
    try:
        with open(json_file) as f:
            raw_content = f.read()
            if not raw_content:
                raise CustomError(f"File {json_file} is empty")
            content: list[dict[str, str]] = loads(raw_content)
            return content
    except FileNotFoundError as e:
        print(f"\033[91mFile not found:\n   - {e}\033[0m")
        quit()
    except JSONDecodeError as e:
        print(f"\033[91mWrong JSON format in {json_file}:\n   - {e}\033[0m")
        quit()
    except CustomError as e:
        print(f"\033[91m{e}\033[0m")
        quit()