# Built-in modules
from enum import Enum
from typing import Self


class Dir(Enum):
    """
    Enum to facilitate the usage of directions in which a wall lies
    Directions are given by first letter and their values are
    corresponding bits.
    """
    N = 0b0001
    E = 0b0010
    S = 0b0100
    W = 0b1000

    @staticmethod
    def reverse(direction: Self) -> dict['Dir', 'Dir']:
        """
        Given a direction a cell returns the opposite

        Args:
            direction (Dir)

        Returns:
            The opposite direction
        """
        options: dict[Dir, Dir] = {Dir.N: Dir.S,
                                   Dir.E: Dir.W,
                                   Dir.S: Dir.N,
                                   Dir.W: Dir.E}
        return options[direction]

    @staticmethod
    def offset(direction: Self) -> tuple[int, int]:
        """
        Given a direction returns the coordinates representing it

        Args:
            direction (Dir)

        Returns:
            Tuple of 
        """
        offsets = {Dir.N: (-1, 0),
                   Dir.E: (0, 1),
                   Dir.S: (1, 0),
                   Dir.W: (0, -1)}
        return offsets[direction]
