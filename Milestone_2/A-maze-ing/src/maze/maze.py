from .cell import DIR, Cell
from src.config_parser import load_maze_config, MazeConfig

class Maze():
    def __init__(self, maze_config: MazeConfig) -> None:
        self.height: int = maze_config.height
        self.width: int = maze_config.width
        self._cells : list[list[Cell]] = []

        for i in range(maze_config.height):
            row: list = []
            for j in range(maze_config.width):
                cell = Cell((i, j))
                row.append(cell)
            self._cells.append(row)



if __name__ == "__main__":
    maze_config = load_maze_config()

    maze: Maze = Maze(maze_config)

    print(maze._cells)