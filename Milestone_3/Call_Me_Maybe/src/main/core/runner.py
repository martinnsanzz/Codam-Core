# Built-in Modules
from random import choice
from json import loads

# Installed modules
import numpy as np

# Local Modules
from llm_sdk import Small_LLM_Model
from .schema import FunctionLookup
from ..classes import Prompt

MAX_TOKENS = 50


# def run_pipeline(prompts: list[Prompt], functions_lookup: FunctionLookup) -> None:
#     small_llm = Small_LLM_Model()

#     for i, prompt_obj in enumerate(prompts): # prompts[:1]
#         answer = small_llm_answer(small_llm, prompt_obj.build_prompt(functions_lookup))
#         print(f"PROMPT NUMBER {i}")
#         print(f"Prompt: {prompt_obj.prompt}", end="\n\n")
#         print(f"AI: {answer}")
#         print("---------------------------------------------")


# def small_llm_answer(small_llm: Small_LLM_Model, prompt: str) -> str:
#     print(prompt)
#     tokenization = small_llm.encode(prompt).tolist()[0]
#     token_len = len(tokenization)

#     for _ in range(0, MAX_TOKENS):
#         logits = small_llm.get_logits_from_input_ids(tokenization)
#         np_lst = np.array(logits)
#         sorted_indices = np_lst.argsort()[-5:]
#         top = {}
#         for i in sorted_indices.tolist():
#             top.update({i: logits[i]})
#         word_id = choice(list(top.keys()))
#         tokenization.append(word_id)
#     return small_llm.decode(tokenization[token_len:])

def test_decoding() -> None:
    small_llm = Small_LLM_Model()

    vocab_path = small_llm.get_path_to_vocab_file()
    with open(vocab_path, 'r') as f:
        vocab_dict: dict[str, int] = loads(f.read())

    id_to_token = {token_id: token_str for token_str, token_id in vocab_dict.items()}


    prompt = "Hello"
    tokenization = small_llm.encode(prompt).tolist()[0]

    for _ in range(5):
        logits = small_llm.get_logits_from_input_ids(tokenization)
        np_array = np.array(logits)

        for token_id in range(len(np_array)):
            token_str = id_to_token.get(token_id, "")
            if not token_str.lstrip("ĠĊ").isdigit():
                np_array[token_id] = -np.inf

        best_id = int(np.argmax(np_array))
        tokenization.append(best_id)
        print(f"Picked token {best_id}: {id_to_token.get(best_id)}")

    print(small_llm.decode(tokenization))