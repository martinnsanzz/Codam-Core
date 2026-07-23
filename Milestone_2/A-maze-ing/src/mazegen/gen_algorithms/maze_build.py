# Build-in modules
from random import Random

# Local modules
from ..classes import Maze
from .kruskal import Kruskal
from .dfs import DFS


def build_kruskal_maze(maze: Maze, rng: Random) -> Maze:
    """Build the maze using the kruskal algorithm."""
    return Kruskal(maze, rng).construct()

def build_dfs_maze(maze: Maze, rng: Random) -> Maze:
    """Build the maze using the dfs algorithm."""
    return DFS(maze, rng).construct()