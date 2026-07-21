# Local Modules
from .base import Maze_Solve
from ..cell_class import Cell


class Maze_Solve_Perfect(Maze_Solve):
    def solve(
            self,
            start: tuple[int, int],
            end: tuple[int, int]) -> str:
        """
        Algorithm to solve a given maze
        Returns the instructions to move from start to end

        Keyword arguments:
        start -- Starting position
        end -- Target position
        """
        dead_cells: set[Cell] = set()
        valid_cells: set[Cell] = set()
        dead_ends = (0b0111, 0b1011, 0b1101, 0b1110)
        valid_cells = {cell
                       for row in self._work_maze.cells
                       for cell in row
                       if not cell.locked}
        start_cell: Cell
        cells_closed: bool = True
        while cells_closed:
            cells_closed = False
            for cell in valid_cells:
                if (cell.walls == 15) or (cell in dead_cells):
                    continue
                if cell.walls in dead_ends:
                    if cell.pos == start:
                        start_cell = cell
                        continue
                    elif cell.pos == end:
                        continue
                    dead_cells.add(cell)
                    self.close_cell(self._work_maze, cell)
                    cell.locked = True
                    cells_closed = True
            valid_cells.difference_update(dead_cells)

        # Print the maze with all cells closed other than the paths
        print(self._work_maze.get_print_string())

        valid_cells.remove(start_cell)
        path: list[tuple[int, int]] = [start]
        moves: list[str] = []
        cell = start_cell
        while valid_cells:
            next_cell, move = self.get_next_cell(self._work_maze, cell)
            valid_cells.remove(next_cell)
            self.close_cell(self._work_maze, cell)
            cell = next_cell
            path.append(cell.pos)
            moves.append(move)

        for r, c in path:
            self._maze.cells[r][c].locked = True
            self._maze.cells[r][c].flag = Cell.FLAG.PATH
        # Print the maze with the path cells locked
        print(self._maze.get_print_string())
        return ("".join(moves))