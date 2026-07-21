#  Built-in module
import random

# Local modules
from ..maze_class import Maze
from ..cell_class import Cell
from ..dir_class import Dir
from .base import Maze_Gen


class Kruskal(Maze_Gen):
    """ This class construcs a maze following the kruskal algorithm.

    Attributes:
        connected (list[set[Cell]]): A list that contains all the cells
                                     that are already connected.
    """
    def __init__(self, maze: Maze) -> None:
        """
        Initializes the Kruskal algorithm which implements additional attributes 
        and variations of the generic Maze_gen class

        Args:
            maze (Maze): Maze object to modify.
        """
        super().__init__(maze)
        self.connected: list[set[Cell]] = []

    def break_wall(self, cell: Cell, direction: Dir, tar_cell: Cell) -> None:
        """Override on the generic break_wall method.
        
        This implements the generic method and merges the paths of the two
        cells that are connected.

        Args:
            cell (Cell) Current cell in focus.
            direction (Dir) Wall to break in the current cell.
            tar_cell (Cell) Cell to open a path to.
        """
        super().break_wall(cell, direction, tar_cell)
        self.merge_connected(cell, tar_cell)

    def get_neighbours(self, cell: Cell) -> list[tuple[Dir, Cell]]:
        """Override on the generic get_neighbours method.

        Get all the neighbours and filter out any that are already

        Args:
            cell (Cell) Cell object to be checked.
        
        Returns:
            A list of tuples with (direction, cell).
        """
        nbs = super().get_neighbours(cell)
        path = self.get_connected(cell)
        nbs = [x for x in nbs if x[1] not in path]
        return nbs

    def merge_connected(self, cell_1: Cell, cell_2) -> None:
        """Merge the paths (set of connected cells) of two cells
        
        Notes:
            This would be invoked when walls are broken
        """
        path_a: set[Cell] | None = None
        path_b: set[Cell] | None = None
        for path in self.connected:
            if cell_1 in path:
                path_a = path
            if cell_2 in path:
                path_b = path
            if (path_a is not None) and (path_b is not None):
                break
        self.connected.remove(path_a)
        self.connected.remove(path_b)
        if (path_a is None) or (path_b is None):
            raise RuntimeError("Cells could not be found in connectivity. "
                               f"{cell_1.loc} {cell_2.loc}")
        self.connected.append(path_a | path_b)

    def get_connected(self, cell: Cell) -> set[Cell]:
        """Gets the path of connected cells

        Args:
            cell (Cell) The cell to be checked.

        Returns:
            A set of all cells connected to the given cell
        """
        for path in self.connected:
            if cell in path:
                return path
        raise Exception("CELL NOT FOUND")

    def construct(self) -> None:
        """
        Expand on this. Check dfs docstring for reference
        """

        all_cells: list[Cell] = list()
        cell: Cell | None = None
        cell_cnt = 0
        for row in self._maze.cells:
            for cell in row:
                if not cell.locked:
                    all_cells.append(cell)
                    self.connected.append({cell})
                    cell_cnt += 1

        i = 0
        path = self.get_connected(cell)
        while len(path) != cell_cnt:
            i += 1
            cell = random.choice([x for x in all_cells if x not in path])
            path = self.get_connected(cell)
            nbs = self.get_neighbours(cell)
            if not len(nbs):
                continue
            tar_dir, tar_cell = random.choice(nbs)
            self.break_wall(cell, tar_dir, tar_cell)

        if not self._maze.maze_config.perfect:
            self.imperfect_maze()
