#!/usr/bin/env python3


import sys
import src


def main(config_file: str) -> None:
    config: dict = src.config_parser(config_file)
    print(config)


if __name__ == "__main__":
    try:
        _, config_file = sys.argv
        if config_file != "config.txt":
            raise src.CustomError("Incorrect argument. Argument \
can only be 'config.txt' (e.g., ./a_maze_ing.py 'context.txt')")
        main(config_file)
    except ValueError:
        src.C().msg("F", "Incorrent command: Too many arguments, only \
'config.txt' is accepted !")
    except src.CustomError as error:
        src.C().msg("F", str(error))

