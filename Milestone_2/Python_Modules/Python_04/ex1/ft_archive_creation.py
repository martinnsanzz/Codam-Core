#!/usr/bin/env python3


import sys


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


def read_file(file: str) -> None:
    f = open(file, "r")
    print("---\n")
    print(f.read())
    print("\n---")
    f.close()
    Colors().print_msg("OKCYAN", f"File '{file}' closed.")


def print_edit_file(file: str) -> None:
    Colors().print_msg("OKCYAN", "\nTransform data:")
    f = open(file, "r")
    text = f.read().split('\n')
    print("---\n")
    for line in text:
        print(line + '#')
    print("\n---")
    f.close()


def safe_edit_file(file: str) -> None:
    print(Colors.OKCYAN, end="")
    file_name = input("Enter new file name (or empty): ")
    print(Colors.ENDC, end="")

    if not file_name:
        Colors().print_msg("WARNING", "Not saving data.")
    if ".txt" not in file_name:
        raise Exception("File extension must be .txt")
    else:
        Colors().print_msg("OKGREEN", f"Saving data to '{file_name}'")
        Colors().print_msg("OKGREEN", f"Data saved in file '{file_name}'")
        f = open(file, "r")
        new_file = open(file_name, "w")
        text = f.read().split('\n')
        index = 0
        for line in text:
            if index != (len(text) - 1):
                new_file.write(line + "#" + '\n')
            else:
                new_file.write(line + "#")
            index += 1
        f.close()
        new_file.close()


def main(file: str) -> None:
    Colors().print_msg("HEADER", "=== Cyber Archives Recovery ===")
    Colors().print_msg("OKCYAN", f"Accesing file '{file}'")
    try:
        read_file(file)
        print_edit_file(file)
        safe_edit_file(file)
    except Exception as error:
        Colors().print_msg("FAIL", f"Error with file: {error}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        Colors().print_msg("WARNING", "Usage: ft_ancient_text.py <file>")
