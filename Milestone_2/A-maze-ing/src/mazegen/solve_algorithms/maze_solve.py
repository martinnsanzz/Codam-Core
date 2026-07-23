# Built-in modules
from copy import deepcopy
from abc import abstractmethod

# Local modules
from ..gen_algorithms.maze_gen import Maze_Gen
from ..classes import Cell, Dir, Maze


class Maze_Solve(Maze_Gen):
    def __init__(self) -> None:
        self.solution = ""
        self.steps: list[tuple[int, int]] = []

    def close_cell(self, maze: Maze, cell: Cell) -> None:
        """
        Fully closes a given cell and modifies the surrounding cells accordingly
        """
        r, c = cell.pos
        for d in list(Dir):
            r_offset, c_offset = Dir.offset(d)
            if not cell.get_wall(d):
                cell.toggle_wall(d)
                tar_cell = maze.cells[r + r_offset][c + c_offset]
                tar_cell.toggle_wall(Dir.reverse(d))
        if cell.walls != 15:
            raise RuntimeError("THIS METHOD DIDNT WORK")

    def construct(self) -> None:
        raise RuntimeError("This is a maze build class")

    @staticmethod
    def cell_to_grid(pos: tuple[int, int]) -> tuple[int, int]:
        return tuple([1 + (2 * x) for x in pos])


    @abstractmethod
    def solve(self, maze: Maze, entry: tuple[int, int], exit: tuple[int, int]):
        """
        Implement the solving algorithm
        """
        pass
