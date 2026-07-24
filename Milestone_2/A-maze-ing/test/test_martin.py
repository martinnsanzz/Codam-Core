# Run from root like this: python3 -m test.test_martin

from src.mazegen.generator import MazeGenerator

if __name__ == "__main__":
    maze = MazeGenerator(10, 10, "dfs", True)

    maze_grid = maze.generate()

    print(maze_grid.get_print_string())