#!/usr/bin/env python3


import sys
import os
from dotenv import load_dotenv # type: ignore


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

    def msg(self, color: str, msg: str) -> None:
        print(getattr(self, color) + msg + C.E)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    debug = os.getenv("DEBUG", "FALSE")

    print(api_key)
    print(debug)