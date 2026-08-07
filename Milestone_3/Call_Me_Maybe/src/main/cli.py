# Built-in Modules
import argparse
from pathlib import Path

# Local Modules
from .loader import load_json
from .classes import Prompt

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
                        default="data/input/functions_definition.json")

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
        prompts = Prompt(args.input)
        functions = load_json(args.functions_definition)

    except argparse.ArgumentError as e:
        print(f"\033[91mIncorrect argument on command line:\n   - {e}\033[0m")