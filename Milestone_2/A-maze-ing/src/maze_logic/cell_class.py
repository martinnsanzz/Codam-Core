# Build-in modules
from typing import Self, Optional
from enum import Enum, auto

# Local modules
from .dir_class import Dir


class Cell():
    def __init__(self, pos: tuple[int, int], value: Optional[int] = 15):
        """
        15 represents the 4 bits we need to describe the walls

        Keyword arguments:
        pos -- (x, y) position of the cell in the 2D array of the maze
        value -- An optional value of what the wall configuration is (0 - 15)
        """
        Cell.validate(value)
        self._walls = value
        self._pos = pos
        self._locked = False
        # self._is_entry_exit: bool = False


    def toggle_wall(self, direction: Dir):
        """
        Given a direction it opens or closes the associated wall

        Keyword arguments:
        direction -- Direction of the wall from the center of the cell
        """
        if self._locked:
            raise RuntimeError("Cell is locked")
        self._walls = self._walls ^ direction.value

    def get_wall(self, direction: Dir) -> bool:
        """
        Return a boolean to describe if there is a wall in a given direction

        Keyword arguments:
        direction -- Direction of the wall from the center of the cell
        """
        return bool(self._walls & direction.value)

    @property
    def locked(self) -> bool:
        """
        Is this cell locked? If yes it cannot be modified.
        """
        return self._locked

    @locked.setter
    def locked(self, lock: bool) -> None:
        """
        Set the lock state of this cell

        Keyword arguments:
        lock -- If True, this cells walls can no longer be modified
        """
        self._locked = lock

    # @property
    # def visited(self) -> bool:
    #     return self._visited
    
    # @visited.setter
    # def visited(self, visit: bool) -> None:
    #     self._visited = visit

    @property
    def walls(self):
        """
        Walls configuration of the cell
        """
        return self._walls

    @walls.setter
    def walls(self, value: int) -> None:
        """
        Set the value of the walls of the cell. This sets ALL walls.

        Keyword arguments:
        value -- 0-15 int to represent the wall configuration
        """
        Cell.validate(value)
        if self._locked:
            raise RuntimeError("Cell is locked")
        self._walls = value

    @property
    def pos(self) -> tuple[int, int]:
        """
        Position of the cell in the maze as given by (x,y) coordinates
        """
        return self._pos

    @property
    def flag(self) -> "Cell.FLAG":
        """
        Return the flag set for this cell
        """
        return self._flag

    @flag.setter
    def flag(self, flag: "Cell.FLAG") -> None:
        """
        Set the flag of this cell to something
        """
        self._flag = flag

    @staticmethod
    def validate(value: int) -> None:
        """
        Validate walls of a cell. Allowed values are 0-15 ints.
        If the value is allowed, nothing happens, otherwise it errors.

        Keyword arguments:
        value -- 0-15 int to represent the wall configuration
        """
        if (value < 0) or (value > 15):
            raise RuntimeError("Cells cannot have values"
                               " outside the range 0-15."
                               f" Provided value is {value}")

    @staticmethod
    def stamp(print_array: list[list[str]], cell: Self) -> None:
        """
        Takes a list of lists of strings (rows[columns]) and stamps the
        surrounding fields around a cell.
        This establishes values for the 4 fields around a given cell.

        Keyword arguments:
        print_array -- A 2D list of rows and columns representing
                       not just the cells but also the walls inbetween them
        cell -- The cell that is checked whose values are to be
                written into the print_array
        """
        row, col = cell.pos
        row = 1 + (row * 2)
        col = 1 + (col * 2)
        wall = ("  ", "██")
        print_array[row - 1][col] = wall[cell.get_wall(Dir.n)]
        print_array[row + 1][col] = wall[cell.get_wall(Dir.s)]
        print_array[row][col + 1] = wall[cell.get_wall(Dir.e)]
        print_array[row][col - 1] = wall[cell.get_wall(Dir.w)]
        print_array[row][col] = ["  ", "░░"][cell.locked]

    # def is_entry_exit(self) -> None:
    #     self._is_entry_exit = True

    class FLAG(Enum):
        """
        Enum to flag if a cell needs to be treated or drawn in a special way
        """
        EMPTY = auto()
        PATH = auto()
        PATTERN = auto()


