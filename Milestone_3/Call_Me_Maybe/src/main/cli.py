# Built-in Modules
import argparse
from pathlib import Path

# Local Modules
from .loader import load_json
from .classes import Prompt
from .runner import run_pipeline
from .utils import CustomError

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
        raw_prompt = load_json(args.test) if args.test else load_json(args.input)
        functions_definition = load_json(args.functions_definition)
        prompts: list[Prompt] = []

        if not raw_prompt:
            raise CustomError("No prompt found. Add a prompt to '.json file'")
        print(functions_definition)
        if isinstance(raw_prompt, list):
            for item in raw_prompt:
                if not item["prompt"]:
                    raise CustomError("Empty prompt found, fix this !!")
                prompts.append(Prompt(prompt=item["prompt"]))
        else:
            if not raw_prompt["prompt"]:
                raise CustomError("Empty prompt found, fix this !!")
            prompts.append(Prompt(prompt=raw_prompt["prompt"]))

        run_pipeline(prompts, functions_definition)
    except argparse.ArgumentError as e:
        print(f"\033[91mIncorrect argument on command line:\n   - {e}\033[0m")
    except KeyError :
        print(f"\033[91mExpected key in '.json file': 'prompt'\033[0m")
    except CustomError as e:
        print(f"\033[91mERROR:\n   - {e}\033[0m")