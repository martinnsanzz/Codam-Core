from .cell import DIR, Cell
from src.config_parser import load_maze_config, MazeConfig


class Maze():
    def __init__(self, maze_config: MazeConfig) -> None:
        self.width: int = maze_config.width
        self.height: int = maze_config.height
        self._cells : list[list[Cell]] = []

        for x in range(maze_config.width):
            row: list = []
            for y in range(maze_config.height):
                cell = Cell((x, y))
                row.append(cell)
            self._cells.append(row)

    def get_neighbors(self, cell: Cell) -> dict[DIR, Cell]:
        cell_x, cell_y = cell.pos
        neighbors = {}
        deltas = {
            DIR.N: (0, -1), # North
            DIR.S: (0, 1),  # South
            DIR.E: (-1, 0), # East
            DIR.W: (1, 0)   # West
        }

        for key, (dx, dy) in deltas.items():
            nx, ny = cell_x + dx, cell_y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.update({key: self._cells[nx][ny]})
        return neighbors

    def get_maze(self) -> list[list[str]]:
        rows = 2 * self.height + 1
        cols = 2 * self.width + 1
        maze: list[list[str]] = [["█" for _ in range(cols)] for _ in range(rows)]

        for x in range(self.width):
            for y in range(self.height):
                cell = self._cells[x][y]

                maze[2 * y + 1][2 * x + 1] = " "
                maze[2 * y][2 * x + 1] = "█" if cell.north else " "
                maze[2 * y + 2][2 * x + 1] = "█" if cell.south else " "
                maze[2 * y + 1][2 * x + 2] = "█" if cell.east else " "
                maze[2 * y + 1][2 * x] = "█" if cell.west else " "
        return maze
