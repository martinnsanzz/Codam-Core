# Built-in Modules
from pathlib import Path

# Local Modules
from ..loader import load_json

class Prompt():
    def __init__(self, prompt_path: Path) -> None:
        self._prompts_json = load_json(prompt_path)
        
        self._prompt: list[str] = []
        for item in self._prompts_json:
            self._prompt.append(item["prompt"])

    def tokenize_prompt
    