#  Built-in module
import random

# Local modules
from src.maze_logic.maze import Maze
from src.maze_logic.cell import Cell
from src.maze_logic.dir import Dir
from src.config_parser import MazeConfig
from .base import Maze_Gen


class DFS(Maze_Gen):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.visited_cells: set[Cell] = set()

    def get_neighbours(self, cell: Cell) -> list[tuple[Dir, Cell]]:
        nbs = super().get_neighbours(cell)

        nbs = [x for x in nbs if not x[1] in self.visited_cells]
        return nbs

    def construct(self) -> None:        
        current_cell: Cell = self.select_rand_cell()
        stack: list[Cell] = []

        self.visited_cells.add(current_cell)
        stack.append(current_cell)

        while stack:
            cell_neighbours = self.get_neighbours(current_cell)

            if cell_neighbours:
                stack.append(current_cell)
                next_cell: tuple[Dir, Cell] = random.choice(cell_neighbours)
                self.visited_cells.add(next_cell[1])
                self.break_wall(current_cell, next_cell[0], next_cell[1])
                current_cell = next_cell[1]
            elif stack:
                current_cell = stack[-1]
                stack.pop()

        if not self._maze.maze_config.perfect:
            self.imperfect_maze()