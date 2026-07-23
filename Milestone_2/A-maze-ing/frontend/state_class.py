# Built-in module
from enum import Enum, auto


class State(Enum):
    """UI Actions. Each constant is a state."""
    QUIT = auto()
    START_WIN = auto()
    GEN_MAZE = auto()
    CHANGE_COLOR = auto()
    SOLVE = auto()

    @staticmethod
    def handle_input(key: str) -> int:
        """Map an uppercase input key to its corresponding state action."""
        actions = {
            "G": State.GEN_MAZE,
            "R": State.GEN_MAZE,
            "C": State.CHANGE_COLOR,
            "Q": State.QUIT,
            "S": State.SOLVE}
        return actions.get(key.upper(), "")
