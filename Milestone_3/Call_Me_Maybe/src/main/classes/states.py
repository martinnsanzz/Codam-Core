# Built-in modules
from enum import Enum, auto


class NumState(Enum):
    START = auto()
    IN_MINUS = auto()
    IN_DOT = auto()
    INT_DIGITS = auto()
    FRAC_DIGITS = auto()
    DONE = auto()


class StrState(Enum):
    OPEN = auto()
    CLOSED = auto()