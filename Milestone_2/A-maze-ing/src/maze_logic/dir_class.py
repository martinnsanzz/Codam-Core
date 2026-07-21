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
    def reverse(d: Self) -> dict['Dir', 'Dir']:
        """Given a direction a cell returns the opposite"""
        options: dict[Dir, Dir] = {Dir.n: Dir.s,
                                   Dir.e: Dir.w,
                                   Dir.s: Dir.n,
                                   Dir.w: Dir.e}
        return options[d]

    @staticmethod
    def offset(d: Self) -> tuple[int, int]:
        """Given a direction returns the offset of it"""
        offsets = {Dir.n: (-1, 0),
                   Dir.e: (0, 1),
                   Dir.s: (1, 0),
                   Dir.w: (0, -1)}
        return offsets[d]
