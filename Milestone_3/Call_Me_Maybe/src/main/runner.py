# Built-in Modules
from typing import TYPE_CHECKING

# Local Modules
from .classes import Prompt

if TYPE_CHECKING:
    from llm_sdk import Small_LLM_Model

def run_pipeline(small_llm: "Small_LLM_Model" ,prompts: list[Prompt],
                 functions: list[dict[str, str]]) -> None:
    prompt = prompts[0]
    tokenization = small_llm.encode(prompt.prompt)
    print(tokenization)
    logits = small_llm.get_logits_from_input_ids(tokenization.tolist()[0])
    logits.sort(reverse=False)
    print(logits)