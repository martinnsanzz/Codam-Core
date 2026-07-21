# Built-in modules
from enum import Enum
from typing import Self


class Dir(Enum):
    """
    Enum to facilitate the usage of directions in which a wall lies
    Directions are given by first letter and their values are
    corresponding bits.
    """
    n = 0b0001
    e = 0b0010
    s = 0b0100
    w = 0b1000

    @staticmethod
    def reverse(d: Self) -> Self:
        """
        Return the inverse of the given direction
        Eg. If north is given, it will return south

        Keyword arguments:
        d -- direction enum
        """
        options: dict[Dir, Dir] = {Dir.n: Dir.s,
                                   Dir.e: Dir.w,
                                   Dir.s: Dir.n,
                                   Dir.w: Dir.e}
        return options[d]

    @staticmethod
    def offset(d: Self) -> tuple[int, int]:
        """
        Return a tuple which indicates the offset a direction represents

        Keyword arguments:
        d -- Direction
        """
        offsets = {Dir.n: (-1, 0),
                   Dir.e: (0, 1),
                   Dir.s: (1, 0),
                   Dir.w: (0, -1)}
        return offsets[d]
