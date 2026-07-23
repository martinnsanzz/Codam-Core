# Build-in modules
from enum import Enum, auto

class Flag(Enum):
    """
    Enum that represents what a pixel should be drawn as.
    The values are:
    EMPTY: An empy cell that is not part of a solution or pattern
    SOLUTION: A cell or a wall that is part of a solution path
    PATTERN: A cell or a wall that is part of a pattern
    WALL: A wall that is not part of a solution or pattern
    """
    EMPTY = auto()
    SOLUTION = auto()
    PATTERN = auto()
    WALL = auto()

class Pixel():
    """
    Class to represent a pixel.
    This is different from the Cell class in that a cell
    represents only a path, whereas the pixel includes
    any walls surrounding that path.
    """
    def __init__(self) -> None:
        self._flags: list[Flag] = []

    def add_flag(self, flag: Flag) -> None:
        self._flags.append(flag)

    def read(self) -> Flag:
        if len(self._flags) == 0:
            return Flag.WALL
        elif len(self._flags) == 1 or len(set(self._flags)) == 1:
            return self._flags[0]
        elif self._flags.count(Flag.SOLUTION) >= 2:
            return Flag.SOLUTION
        elif self._flags.count(Flag.PATTERN) >= 2:
            return Flag.PATTERN
        elif Flag.SOLUTION in self._flags and Flag.EMPTY in self._flags:
            return Flag.EMPTY
        else:
            return Flag.WALL
