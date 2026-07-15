#!/usr/bin/env python3

from src.maze.maze import Maze
from src import load_maze_config

if __name__ == "__main__":
    maze_config = load_maze_config()

    maze: Maze = Maze(maze_config)

    print(maze._cells)