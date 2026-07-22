# Global modules
from copy import deepcopy

# Local modules
from ..classes import Cell, Dir, Maze, Flag
from .maze_solve import Maze_Solve

class Maze_Solve_Perfect(Maze_Solve):
    def get_next_cell(self, maze: Maze, cell: Cell) -> tuple[Cell, Dir]:
        """
        Return the cell next to the given cell that is directly connected
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
                return (maze.cells[row][col], wall)
        raise RuntimeError(f"No neighbours found for {cell.pos}")


    def solve(self, maze: Maze) -> str:
        """
        Algorithm to solve a given maze
        Returns the instructions to move from start to end
        """
        work_maze = deepcopy(maze)
        start = maze.maze_config.entry
        end = maze.maze_config.exit
        dead_cells: set[Cell] = set()
        valid_cells: set[Cell] = set()
        dead_ends = (0b0111, 0b1011, 0b1101, 0b1110)
        valid_cells = {cell
                       for row in work_maze.cells
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
                    self.close_cell(work_maze, cell)
                    cell.locked = True
                    cells_closed = True
            valid_cells.difference_update(dead_cells)

        valid_cells.remove(start_cell)
        path: list[tuple[int, int]] = [start]
        moves: list[str] = []
        self.steps = [Maze_Solve.cell_to_grid(start)]
        cell = start_cell
        while valid_cells:
            next_cell, move = self.get_next_cell(work_maze, cell)
            valid_cells.remove(next_cell)
            self.close_cell(work_maze, cell)
            grid_pos = self.steps[-1]
            wall_pos = (grid_pos[0] + Dir.offset(move)[0],
                        grid_pos[1] + Dir.offset(move)[1])
            self.steps.append(wall_pos)
            self.steps.append(Maze_Solve.cell_to_grid(next_cell.pos))
            cell = next_cell
            path.append(cell.pos)
            moves.append(move.name.upper())
        self.solution = "".join(moves)

        for r, c in path:
            maze.cells[r][c].flag = Flag.SOLUTION
        return self.solution