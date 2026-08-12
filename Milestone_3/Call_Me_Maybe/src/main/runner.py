# Built-in Modules
from typing import TYPE_CHECKING
import numpy as np
from random import choice

# Local Modules
from .classes import Prompt

if TYPE_CHECKING:
    from llm_sdk import Small_LLM_Model

MAX_TOKENS = 100

def run_pipeline(small_llm: "Small_LLM_Model" ,prompts: list[Prompt],
                 functions: list[dict[str, str]]) -> None:
    prompt = prompts[0]
    tokenization = small_llm.encode(prompt.prompt).tolist()[0]
    for _ in range(0, MAX_TOKENS):
        logits = small_llm.get_logits_from_input_ids(tokenization)
        np_lst = np.array(logits)
        sorted_indices = np_lst.argsort()[-5:]
        word = choice(sorted_indices.tolist())
        # max_words = max(range(len(logits)), key=logits.__getitem__)
        tokenization.append(word)
        # sorted_list = sorted(logits, reverse=True)[:10]
    print(f"Prompt is: {prompt.prompt}")
    print("AI answer: ", end="")
    print(small_llm.decode(tokenization[len(prompt.prompt):]))
