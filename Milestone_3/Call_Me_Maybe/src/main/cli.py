# Built-in Modules
from argparse import Namespace, ArgumentParser, ArgumentError
from pathlib import Path
from typing import TypeAlias, Any
import re

# Local Modules
from .exceptions import CustomError
from .classes import Prompt
from .loader import load_json
from .schema import build_function_lookup
from .runner import run_pipeline

FunctionLookup: TypeAlias = dict[str, dict[str, Any]]

def _main() -> None:
    try:
        args = args_parser()
        prompts, functions_lookup = setup_pipeline(args)

        run_pipeline(prompts)
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


def setup_pipeline(args: Namespace) -> tuple[list[Prompt], FunctionLookup]:
    prompt_json = load_json(args.test) if args.test else load_json(args.input)
    functions_json = load_json(args.functions_definition)

    prompts = Prompt.from_json(prompt_json)
    functions_lookup = build_function_lookup(functions_json)

    return (prompts, functions_lookup)
