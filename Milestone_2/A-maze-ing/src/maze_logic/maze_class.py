# Built-in modules
import random
from typing import Self

# Local modules
from src import MazeConfig, CustomError
from .cell_class import Cell


class Maze():
    """This class represents the maze grid based on `config.txt`.
    
    Attributes:
        maze_config (MazeConfig): A copy of the maze configuration to be used
                                  where needed.
        _width (int): Width of maze.
        _height (int): Height of maze.
        _cells (list[list[Cell]]): A 2D list of the cells from the maze.
    """
    def __init__(self, maze_config: MazeConfig) -> None:
        """Initialise a new maze based on maze config.

        Args:
            maze_config (MazeConfig): Maze configuration extracted 
                                      from `config.txt`.
        
        Notes:
            Calls random.seed(mazed_condif.seed) to mantain Reproducibility
            across calls.                     
        """
        self.maze_config = maze_config
        self._width: int = maze_config.width
        self._height: int = maze_config.height
        self._cells : list[list[Cell]] = []
        random.seed(maze_config.seed)

        row: list[Cell]
        cell: Cell
        for x in range(maze_config.height):
            row: list = []
            for y in range(maze_config.width):
                cell = Cell((x, y))
                row.append(cell)
            self._cells.append(row)

    def lock_42_cells(self) -> None:
        """Close and lock all the cells that need to draw 42."""
        if (self._width < 9) or (self._height < 7):
            print("Maze is too small for the 42 sign")
            return
        centre_x: int = int(self._width / 2)
        centre_y: int = int(self._height / 2)
        start_col = centre_x - 3
        start_row = centre_y - 2
        cols = [[0, 2, 4, 5, 6],
                [0, 2, 6],
                [0, 1, 2, 4, 5, 6],
                [2, 4],
                [2, 4, 5, 6]]
        for row in range(0, 5):
            for col in range(0, 7):
                if col in cols[row]:
                    cell = self.cells[start_row + row][start_col + col]
                    try:
                        cell.walls = 15
                        cell.locked = True
                    except RuntimeError:
                        pass

    def get_print_string(self) -> str:
        """Converts the maze from a list[list[Cell] to a string."""
        return "\n".join("".join(x) for x in self.get_maze())

    @property
    def cells(self) -> list[list[Cell]]:
        """Returns the 2D list of Cells."""
        return self._cells

    @cells.setter
    def cells(self, values: list[list[int]]) -> None:
        """Set the cells on the maze cells to the given wall value

        Args:
            values (list[list[int]]): 2D array of integer values holding the 
                                      value of the walls
        Raises:
            Error if values are bigger than height or width of maze.
        """
        if len(values) != self._height:
            raise CustomError("The height of the provided values does "
                               "not match the height of the maze. "
                               f"Given: {len(values)}, "
                               f"expected: {self._height}")
        for y, row in enumerate(self._cells):
            if len(row) != self._width:
                raise CustomError("The width of the provided values does"
                                   "not match the width of the maze. "
                                    f"Given: {len(values)}, "
                                    f"expected: {self._width}")
            for x, cell in enumerate(row):
                cell.walls = values[y][x]

    @property
    def size(self) -> tuple[int, int]:
        """The size of the maze in walkable cells."""
        return (self._width, self._height)

    def get_maze(self) -> list[list[str]]:
        """Build the visual grid representation of the maze for curses.

        Constructs a grid of wall blocks sized according to the maze's
        width and height, then stamps each cell onto the grid to carve
        out paths.

        Returns:
            A 2D grid of strings representing the maze, where each 
            cell is either a wall block ("██") or a path character
        """
        col_cnt = (self._width * 2) + 1
        row_cnt = (self._height * 2) + 1
        output: list[list[str]] = []
        for _ in range(row_cnt):
            row = []
            for __ in range(col_cnt):
                row.append("██")
            output.append(row)

        for row in self._cells:
            for cell in row:
                Cell.stamp(output, cell)
        return output

    @classmethod
    def from_string(cls, hex_str: str) -> Self:
        """ Read a hex string and convert it to a maze object.

        Args:
            hex_str (str) String of a maze represented by hex values
                          of the walls of the cells.
        Returns:
            A new maze object based on the hex_str.
        """
        if len(hex_str.strip("\n0123456789abcdefABCDEF")):
            raise RuntimeError("The input contains unexpected characters")
        rows: list[str] = hex_str.split("\n")
        values: list[list[int]] = []
        for row in rows:
            values.append([int(x, 16) for x in row])

        w: int = len(values[0])
        h: int = len(values)
        maze = Maze(w, h, values)
        return maze