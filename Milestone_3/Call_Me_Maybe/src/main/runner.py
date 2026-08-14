# Built-in Modules
from typing import TYPE_CHECKING
import numpy as np
from random import choice

# Local Modules
from .classes import Prompt
from llm_sdk import Small_LLM_Model

MAX_TOKENS = 50

def run_pipeline(prompts: list[Prompt],
                 functions: list[dict[str, str]]) -> None:
    small_llm = Small_LLM_Model()

    for i, prompt_obj in enumerate(prompts): # prompts[:1]
        answer = small_llm_answer(small_llm, prompt_obj.prompt)
        print(f"PROMPT NUMBER {i}")
        print(f"Prompt: {prompt_obj.prompt}", end="\n\n")
        print(f"AI: {answer}")
        print("---------------------------------------------")


def small_llm_answer(small_llm: Small_LLM_Model, prompt: str) -> str:
    tokenization = small_llm.encode(prompt).tolist()[0]

    for _ in range(0, MAX_TOKENS):
        logits = small_llm.get_logits_from_input_ids(tokenization)
        np_lst = np.array(logits)
        sorted_indices = np_lst.argsort()[-5:]
        top = {}
        for i in sorted_indices.tolist():
            top.update({i: logits[i]})
        word_id = choice(list(top.keys()))
        tokenization.append(word_id)
    return small_llm.decode(tokenization[len(prompt):])