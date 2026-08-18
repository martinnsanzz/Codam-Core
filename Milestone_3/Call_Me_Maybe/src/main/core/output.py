# Built-in modules
from json import dump, loads
from typing import Any
from pathlib import Path

# Local modules


def write_output(output_file: Path, llm_output: str) -> None:
    json_content = loads(llm_output)

    with open(output_file, 'w') as f:
        dump(json_content, fp=f, indent=4)