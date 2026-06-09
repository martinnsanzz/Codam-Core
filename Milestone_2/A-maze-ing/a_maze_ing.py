#!/usr/bin/env python3


import sys


class C:
    H = '\033[95m'  # Header
    B = '\033[94m'  # Blue
    C = '\033[96m'  # Cyan
    G = '\033[92m'  # Green
    W = '\033[93m'  # Warning
    F = '\033[91m'  # Fail
    E = '\033[0m'  # End
    Bo = '\033[1m'  # Bold
    U = '\033[4m'

    def msg(self, color: str, msg: str):
        print(getattr(self, color) + msg + C.E)


class CustomError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def main(argv):
    print("inside")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "config.txt":
        try:
            main(sys.argv)
        except CustomError as error:
            C().msg("F", str(error))
    else:
        C().msg("F", "Incorrect command. Usage: ./a_maze_ing.py context.txt \
or python3 a_maze_ing.py context.txt")
