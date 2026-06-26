#!/usr/bin/env python3

# Built-in modules
import sys
import curses

# Local modules
from src import C, CustomError
import ui


def main() -> None:
    curses.wrapper(ui.main)


if __name__ == "__main__":
    try:
        _, config_file = sys.argv
        if config_file != "config.txt":
            raise CustomError("Incorrect argument. Argument \
can only be 'config.txt' (e.g., ./a_maze_ing.py 'context.txt')")
        main()
    except ValueError:
        C().msg("F", "Incorrent command: Too many arguments, only \
'config.txt' is accepted !")
    except CustomError as error:
        C().msg("F", str(error))
