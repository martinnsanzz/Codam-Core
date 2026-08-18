# Built-in modules
from json import dump, loads
from pathlib import Path


def write_output(output_file: Path, llm_output: list[str]) -> None:
    with open(output_file, 'w') as f:
        llm_formated = [loads(obj) for obj in llm_output]
        dump(llm_formated, fp=f, indent=4)