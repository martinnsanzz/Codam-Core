# Built-in modules
import random
from typing import Self

# Local modules
from src import MazeConfig
from .cell_class import Cell


class Maze():
    def __init__(self, maze_config: MazeConfig) -> None:
        """
        Initialise a new maze based on maze config.

        Parameters:
            - maze_config: Maze configuration extracted from config.txt
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
        """
        Close and lock all the cells that need to draw 42
        """
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
        """
        Return the print string for the maze.
        This refers to the string that draws the maze, not the hexadecimal
        representation
        """
        output: list[list[str]] = []
        output = self.get_maze()
        out_string = "\n".join("".join(x) for x in output)
        return out_string

    @property
    def cells(self) -> list[list[Cell]]:
        """
        2D list of cells in the maze
        """
        return self._cells

    @cells.setter
    def cells(self, values: list[list[int]]) -> None:
        """
        Set the cells of the cells to the given values in the 2D array

        Keyword arguments:
        values -- 2D array of integer values holding the value of the walls
        """
        if len(values) != self._height:
            raise RuntimeError("The height of the provided values does "
                               "not match the height of the maze. "
                               f"Given: {len(values)}, "
                               f"expected: {self._height}")
        for y, row in enumerate(self._cells):
            if len(row) != self._width:
                raise RuntimeError("The width of the provided values does"
                                   "not match the width of the maze. "
                                    f"Given: {len(values)}, "
                                    f"expected: {self._width}")
            for x, cell in enumerate(row):
                cell.walls = values[y][x]

    @property
    def size(self) -> tuple[int, int]:
        """
        The size of the maze in walkable cells
        """
        return (self._width, self._height)

    def get_maze(self) -> list[list[str]]:
        """
        Return the print 2D list of strings for the maze.
        This refers to the string that draws the maze, not the hexadecimal
        representation
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
        """
        Read a hex string and convert it to a maze object

        Keyword arguments:
        hex_str -- String of a maze represented by hex values
                   of the walls of the cells
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