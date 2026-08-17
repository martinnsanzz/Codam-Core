# Built-in Modules
import argparse
from pathlib import Path
import re

# Local Modules
from .loader import load_json, check_prompt_json, build_function_lookup
from .runner import run_pipeline
from .utils import CustomError
from .schema import check_regex

def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
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
        raise argparse.ArgumentError(None,
                                "Correct usage: src [--functi"
                                "ons_definition <FUNCTIONS_DEFINITION>] "
                                "[--input <INPUT>] [--output <OUTPUT>]")
    return args

def _main() -> None:
    try:
        args = args_parser()
        prompt_json = load_json(args.test) if args.test else load_json(args.input)
        functions_json = load_json(args.functions_definition)

        prompts = check_prompt_json(prompt_json)
        functions_lookup = build_function_lookup(functions_json)

        regex = check_regex("string")
        print(regex.pattern)
        print(re.match(regex, '"hello"'))
        # run_pipeline(prompts)
    except argparse.ArgumentError as e:
        print(f"\033[91mIncorrect argument on command line:\n   - {e}\033[0m")
        quit()
    except KeyError :
        print(f"\033[91mExpected key in '.json file': 'prompt'\033[0m")
        quit()
    except CustomError as e:
        print(f"\033[91mERROR:\n   - {e}\033[0m")
        quit()