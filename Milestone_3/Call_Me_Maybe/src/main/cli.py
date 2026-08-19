# Built-in Modules
from argparse import Namespace, ArgumentParser, ArgumentError
from pathlib import Path
import time

# Local Modules
from llm_sdk import Small_LLM_Model
from .classes import Prompt
from .core import load_json, build_function_lookup, Engine, write_output, CustomError




def _main() -> None:
    try:
        # test()
        # start = time.time()
        args = args_parser()
        engine = setup_engine(args)
        llm_output = engine.prompt_loop()

        write_output(args.output, llm_output)
        # end = time.time()
        # print(f"\nTotal runtime of program: {end - start}")
    except ArgumentError as e:
        print(f"\033[91mIncorrect argument on command line:\n   - {e}\033[0m")
        quit()
    except KeyError :
        print(f"\033[91mExpected key in '.json file': 'prompt'\033[0m")
        quit()
    except CustomError as e:
        print(f"\033[91mERROR:\n   - {e}\033[0m")
        quit()

def test():
    num = "5.0"
    print(num.isdigit())
    # small_llm = Small_LLM_Model()

    # prompt = "2.hello0"
    # tokeniazer = small_llm.encode(prompt).tolist()[0]

    # print(tokeniazer)
    # for token in tokeniazer:
    #     print(f"Token '{token}': '{small_llm.decode([token])}'")


def args_parser() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--functions_definition",
                        type=Path,
                        default="data/input/functions_definition.json")
    parser.add_argument("--input",
                        type=Path,
                        default="data/input/function_calling_tests.json")
    parser.add_argument("--output",
                        type=Path,
                        default="data/output/function_calling_results.json")
    parser.add_argument("--test",
                        type=Path,
                        default=None)

    args, argv = parser.parse_known_args()

    if argv:
        raise ArgumentError(None,
                                "Correct usage: src [--functi"
                                "ons_definition <FUNCTIONS_DEFINITION>] "
                                "[--input <INPUT>] [--output <OUTPUT>]")
    return args


def setup_engine(args: Namespace) -> Engine:
    small_llm = Small_LLM_Model()

    prompt_json = load_json(args.test) if args.test else load_json(args.input)
    functions_json = load_json(args.functions_definition)

    functions_lookup = build_function_lookup(functions_json)

    prompts: list[Prompt] = []
    for item in prompt_json:
        prompt = Prompt(prompt=item["prompt"].rstrip("?."))

        prompts.append(prompt)

    engine = Engine(
        prompts=prompts,
        functions_lookup=functions_lookup,
        small_llm=small_llm
    )

    return engine
