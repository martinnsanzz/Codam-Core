# Built-in modules
from abc import ABC, abstractmethod
import random

# Local modules
from src.utils import CustomError
from ..cell_class import Cell
from ..maze_class import Maze
from ..dir_class import Dir


class Maze_Gen(ABC):
    """ This abstract class provides the required attributes and methods
    for any algorithm that inherits from it.

    Attributes:
       _maze (Maze): Maze object to modify.
       open_cells (set[Cell]): A set of cells with more than 1 wall open used
                               to build an imperfect maze
    """
    def __init__(self, maze: Maze) -> None:
        """
        Generic maze generation class that can serve as base for various algorithms.

        Args:
            maze (Maze) Maze object to be modified.
        """
        super().__init__()
        self._maze: Maze = maze
        self._maze.lock_42_cells()
        self.open_cells: set[Cell] = set()

    @abstractmethod
    def construct(self) -> None:
        """Function to build or construct the maze."""
        pass

    def get_neighbours(self, cell: Cell) -> list[tuple[Dir, Cell]]:
        """
        Get all the neighbours the current cell.

        Args:
            cell (Cell) Cell object to be checked.
        
        Returns:
            A list of tuples with (direction, cell).
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

        Args:
            cell (Cell) Current cell in focus.
            direction (Dir) Wall to break in the current cell.
            tar_cell (Cell) Cell to open a path to.
        
        Raises:
            Error if walls are misaligned or if the wall has already being
            broken.
        """
        tar_dir = Dir.reverse(direction)
        if(cell.get_wall(direction) != tar_cell.get_wall(tar_dir)):
            raise CustomError("Aborting gen due to unmatched walls")
        elif(not cell.get_wall(direction)):
            raise CustomError("Wall has already been broken")
        cell.toggle_wall(direction)
        tar_cell.toggle_wall(tar_dir)

    def select_rand_cell(self) -> Cell:
        """
        Selects a random cell from the list of cells.
        
        Note:
            Keeps selecting a cell until the choosen cell is not locked.
        """
        cell: Cell = None

        while not cell:
            cell = random.choice(random.choice(self._maze.cells))
            if cell.locked:
                cell = None

        return cell
    
    def count_not_locked(self) -> int:
        """Counts number of locked cells in the maze."""
        return len([x for x in self._maze.cells for y in x if not y.locked])

    def is_dead_end(self, cell: Cell) -> bool:
        """
        Checks if the cell is a dead_end based on the walls value of the cell.

        Args:
            cell (Cell): Cell to check.
        
        Returns:
            True if is a dead end or False if not.
        
        Note:
            If cell only has 1 neighbours but only one wall open its not considered
            a dead end. Its a cell surrounded by blocked cells (Probably inside the
            42 pattern).
        """
        dead_ends = (0b0111, 0b1011, 0b1101, 0b1110)

        cell_neighbours = Maze_Gen.get_neighbours(self, cell)

        if len(cell_neighbours) <= 1:
            return False
        return cell.walls in dead_ends

    def imperfect_maze(self) -> None:
        """
        Converts a perfect maze into a 'perfectly imperfect' maze () dead ends 
        in total.
            1. Selects a random cell of the maze to start from.
            2. If not dead end_cell adds to list of open_cells.
            3. Loops until open_cells is equal to total not_locked cells.
                3a. If cell is dead_end open a random wall based on the available
                    neighbours and then add it to open_cells[].
                3b. If not dead end add it to open_cells[] and select a
                    neighhbour to be the next cell.
        """
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
