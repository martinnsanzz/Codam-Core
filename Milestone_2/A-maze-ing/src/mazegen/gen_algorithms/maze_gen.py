# Built-in modules
from abc import ABC, abstractmethod
from random import Random

# Local modules
from ..classes import Cell, Dir, Maze


class Maze_Gen(ABC):
    """ This abstract class provides the required attributes and methods
    for any algorithm that inherits from it.

    Attributes:
       _maze (Maze): Maze object to modify.
    """
    def __init__(self, maze: Maze, rng: Random) -> None:
        """
        Generic maze generation class that can serve as base for various algorithms.

        Args:
            maze (Maze) Maze object to be modified.
        """
        super().__init__()
        self._maze: Maze = maze
        self._rng = rng
        self._maze.lock_42_cells()

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
            raise RuntimeError("Aborting gen due to unmatched walls")
        elif(not cell.get_wall(direction)):
            raise RuntimeError("Wall has already been broken")
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
            cell = self._rng.choice(self._rng.choice(self._maze.cells))
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
            1. Loop through the array of cell (colxrow).
            2. Check for neighbours of current cell.
            3. If current cell is a dead_end choose a valid neighbour and break a wall
               between the cells.
        """
        for row in range(self._maze._width):
            for col in range(self._maze._height):
                current_cell = self._maze._cells[col][row]
                cell_neighbours = Maze_Gen.get_neighbours(self, current_cell)
                if self.is_dead_end(current_cell):
                    while self.is_dead_end(current_cell):
                        neigbour = self._rng.choice(cell_neighbours)
                        if current_cell.get_wall(neigbour[0]):
                            Maze_Gen.break_wall(self, current_cell, neigbour[0], 
                                                neigbour[1])
