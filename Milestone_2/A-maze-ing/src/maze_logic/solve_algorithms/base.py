# Built-in modules
from copy import deepcopy
from abc import abstractmethod

# Local modules
from ..cell_class import Cell
from ..maze_class import Maze
from ..dir_class import Dir
from ..gen_algorithms.base import Maze_Gen


class Maze_Solve(Maze_Gen):
    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)
        self._work_maze = deepcopy(maze)

    def close_cell(self, maze: Maze, cell: Cell) -> None:
        """
        Fully closes a given cell and modifies the surrounding cells accordingly
        """
        r, c = cell.pos
        for d in list(Dir):
            r_offset, c_offset = Dir.offset(d)
            if not cell.get_wall(d):
                cell.toggle_wall(d)
                tar_cell = self._work_maze.cells[r + r_offset][c + c_offset]
                tar_cell.toggle_wall(Dir.reverse(d))
        if cell.walls != 15:
            raise RuntimeError("THIS METHOD DIDNT WORK")

    def get_next_cell(self, maze: Maze, cell: Cell) -> tuple[Cell, str]:
        """
        Return the cells next to the given cell that is directly connected
        as well as the direction it lies in (as a string)
        These two values are packed as a tuple
        This method only works if there is exactly one connected cell

        Keyword arguments:
        maze -- Maze object
        cell -- Current cell in focus
        """

        for wall in list(Dir):
            if not cell.get_wall(wall):
                row = cell.pos[0] + Dir.offset(wall)[0]
                col = cell.pos[1] + Dir.offset(wall)[1]
                return (maze.cells[row][col], wall.name.upper())
        raise RuntimeError(f"No neighbours found for {cell.pos}")

    def construct(self) -> None:
        raise RuntimeError("This is a maze build class")


    @abstractmethod
    def solve(self):
        """
        Implement the solving algorithm
        """
        pass
