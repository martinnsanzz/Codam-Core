# Built-in module
from enum import Enum, auto


class State(Enum):
    """UI Actions. Each constant is a state."""
    QUIT = auto()
    START_WIN = auto()
    GEN_MAZE = auto()
    REGEN = auto()
    CHANGE_COLOR = auto()
