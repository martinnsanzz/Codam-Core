#!/usr/bin/env python3


import sys
import typing


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def print_msg(self, color: str, msg: str):
        print(getattr(self, color) + msg + Colors.ENDC)


def read_file(content: typing.IO) -> str:
    return content.read()


def main(argv: list) -> None:
    Colors().print_msg("HEADER", "=== Cyber Archives Recovery ===")
    try:
        Colors().print_msg("OKCYAN", f"Accesing file '{argv[1]}'")
        content = open(argv[1], 'r')
        print(read_file(content))
        content.close()
        Colors().print_msg("OKCYAN", f"File '{argv[1]}' closed.")
    except Exception as error:
        Colors().print_msg("FAIL", f"Error opening file '{argv[1]}': {error}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        Colors().print_msg("WARNING", "Usage: ft_ancient_text.py <file>")
