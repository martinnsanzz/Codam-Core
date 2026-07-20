# Built-in modules
from abc import ABC, abstractmethod
import random

# Local modules
from ..cell import Cell
from ..maze import Maze
from ..dir import Dir


class Maze_Gen(ABC):
    def __init__(self, maze: Maze) -> None:
        """
        Generic maze generation class that can serve as base for various algorithms

        Keyword arguments:
        maze -- Maze object to be modified
        """
        super().__init__()
        self._maze: Maze = maze
        self._maze.lock_42_cells()
        self.open_cells: set[Cell] = set()

    @abstractmethod
    def construct(self) -> None:
        """
        Function to build or construct the maze
        """
        pass

    def get_neighbours(self, cell: Cell) -> list[tuple[Dir, Cell]]:
        """
        Get all the neighbours the current cell.
        Returns a list of tuples with (direction, cell)

        Keyword arguments:
        cell -- Cell object to be checked
        """
        row, col = cell.pos
        nbs: list[tuple[Dir, Cell]] = []
        nb: Cell
        for d in list(Dir):
            i, j = Dir.offset(d)
            if ((row + i) == -1) or ((col + j) == -1):
                continue
            try:
                nb = self._maze.cells[row + i][col + j]
            except IndexError:
                continue
            if not nb.locked:
                nbs.append((d, nb))
        return nbs

    def break_wall(self, cell: Cell, direction: Dir, tar_cell: Cell) -> None:
        """
        Break a wall of a given cell, and the one of its counterpart.
        Error if walls are missaligned.
        Do nothing if walls are already broken

        Keyword arguments:
        cell -- Current cell in focus
        direction -- Wall to break in the current cell
        tar_cell -- Cell to open a path to
        """
        tar_dir = Dir.reverse(direction)
        if(cell.get_wall(direction) != tar_cell.get_wall(tar_dir)):
            raise RuntimeError("Aborting gen due to unmatched walls")
        elif(not cell.get_wall(direction)):
            raise RuntimeError("Wall has already been broken")
        cell.toggle_wall(direction)
        tar_cell.toggle_wall(tar_dir)

    def select_rand_cell(self) -> Cell:
        cell: Cell = None

        while not cell:
            cell = random.choice(random.choice(self._maze.cells))
            if cell.locked:
                cell = None

        return cell
    
    def count_not_locked(self) -> int:
        return len([x for x in self._maze.cells for y in x if not y.locked])

    def is_dead_end(self, cell: Cell) -> int:
        dead_ends = (0b0111, 0b1011, 0b1101, 0b1110)

        cell_neighbours = Maze_Gen.get_neighbours(self, cell)

        if len(cell_neighbours) <= 1:
            return False
        return cell.walls in dead_ends

    def imperfect_maze(self) -> None:
        current_cell: Cell = self.select_rand_cell()
        if not self.is_dead_end(current_cell):
            self.open_cells.add(current_cell)

        while len(self.open_cells) != self.count_not_locked():
            cell_neighbours = Maze_Gen.get_neighbours(self, current_cell)

            if self.is_dead_end(current_cell):
                while self.is_dead_end(current_cell):
                    next_cell: tuple[Dir, Cell] = random.choice(cell_neighbours)
                    if current_cell.get_wall(next_cell[0]):
                        Maze_Gen.break_wall(self, current_cell, next_cell[0], next_cell[1])
                self.open_cells.add(current_cell)
                current_cell = next_cell[1]
            else:
                self.open_cells.add(current_cell)
                next_cell: tuple[Dir, Cell] = random.choice(cell_neighbours)
                current_cell = next_cell[1]
