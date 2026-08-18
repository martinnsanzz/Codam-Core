# Built-in Modules
from argparse import Namespace, ArgumentParser, ArgumentError
from pathlib import Path

# Local Modules
from .exceptions import CustomError
from .classes import Prompt
from .core import load_json, build_function_lookup, Engine, write_output
from llm_sdk import Small_LLM_Model

from .core.runner import test_decoding


def _main() -> None:
    try:
        args = args_parser()
        # engine = setup_engine(args)

        test_decoding()
        # test = '{"name": "fn_add_numbers", "parameters": {"a": 2.0, "b": 3.0}}'
        # write_output(args.output, test)

    except ArgumentError as e:
        print(f"\033[91mIncorrect argument on command line:\n   - {e}\033[0m")
        quit()
    except KeyError :
        print(f"\033[91mExpected key in '.json file': 'prompt'\033[0m")
        quit()
    except CustomError as e:
        print(f"\033[91mERROR:\n   - {e}\033[0m")
        quit()


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
        prompt = Prompt(prompt=item["prompt"])
        prompt.build_prompt(functions_lookup)

        prompts.append(prompt)

    engine = Engine(
        prompts=prompts,
        functions_lookup=functions_lookup,
        small_llm=small_llm
    )

    return engine
