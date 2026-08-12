# Built-in Modules
from typing import TYPE_CHECKING

# Local Modules
from .classes import Prompt

if TYPE_CHECKING:
    from llm_sdk import Small_LLM_Model

MAX_TOKENS = 50

def run_pipeline(small_llm: "Small_LLM_Model" ,prompts: list[Prompt],
                 functions: list[dict[str, str]]) -> None:
    prompt = prompts[0]
    tokenization = small_llm.encode(prompt.prompt).tolist()[0]
    for _ in range(0, MAX_TOKENS):
        logits = small_llm.get_logits_from_input_ids(tokenization)
        word = max(range(len(logits)), key=logits.__getitem__)
        tokenization.append(word)

    print(small_llm.decode(tokenization))
