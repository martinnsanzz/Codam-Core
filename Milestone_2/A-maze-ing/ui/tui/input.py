# Local module
from ..state import State


def handle_input(key: str) -> int:
    """Map an uppercase input key to its corresponding state action."""
    actions = {
        "G": State.GEN_MAZE,
        "R": State.REGEN,
        "C": State.CHANGE_COLOR,
        "Q": State.QUIT}
    return actions.get(key, "")
