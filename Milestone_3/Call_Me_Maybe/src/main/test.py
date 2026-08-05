# Local modules
from llm_sdk import Small_LLM_Model

def testing(prompts: list[dict[str, str]], functions: list[dict[str, str]]) -> None:
    mod_instance = Small_LLM_Model()

    for prompt in prompts:
        tensor = mod_instance.encode(prompt["prompt"])


        decode = mod_instance.decode(tensor)
        print(decode)