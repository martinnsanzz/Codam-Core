# Built-in modules
from subprocess import call 
import os
from typing import TYPE_CHECKING
from json import dumps

# Local modules
from .ascii_art import CALL_ME_MAYBE_ASCII

if TYPE_CHECKING:
    from ..classes import Prompt

class C:
    """Format regular strings based on color input"""
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


def display_title() -> None:
    """Clears terminal screen and displays title"""
    call('clear' if os.name == 'posix' else 'cls')
    print()
    C().msg("H", str(CALL_ME_MAYBE_ASCII))

def display_prompt_info(prompt_obj: 'Prompt', index: int,
                        total_time: float) -> None:
    """Display prompt information with color when called"""
    C().msg("Bo", f"\n================ Prompt {index} ====================\n\n")

    print(f"\033[93mPrompt: \033[0m'{prompt_obj.prompt}'")
    print(f"\033[93mFunction name: \033[0m'{prompt_obj.name}'")
    print(f"\033[93mParameters: \033[0m'{dumps(prompt_obj.parameters)}", end="\n\n")

    print(f"\033[93mTotal time: \033[92m'{total_time}'\033[0m")
    C().msg("Bo", f"\n==============================================")
