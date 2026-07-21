# Local Modules
from src.maze_logic.gen_algorithms.kruskal import Kruskal
from src.maze_logic.gen_algorithms.dfs import DFS
from src.config_parser import MazeConfig
from .maze_class import Maze

def select_gen_algorithm(maze_config: MazeConfig) -> Maze:
    """
    Select and build a maze based on the passed alghorithm in the
    config.txt
    
    Args:
        maze_config (MazeConfig): Configuration of the file as an object.
    
    Returns:
        `maze` as a Maze object with the modified cells to represent the
        maze grid.
    """
    algorithm_name: str = maze_config.algorithm

    if algorithm_name == "kruskal":
        maze = build_kruskal_maze(maze_config)
    elif algorithm_name == "dfs":
        maze = build_dfs_maze(maze_config)
    return maze

def build_kruskal_maze(maze_config: MazeConfig) -> Maze:
    """Build the maze using the kruskal algorithm."""
    maze = Maze(maze_config)
    builder = Kruskal(maze)
    builder.construct()
    return maze

def build_dfs_maze(maze_config: MazeConfig) -> Maze:
    """Build the maze using the dfs algorithm."""
    maze = Maze(maze_config)
    builder = DFS(maze)
    builder.construct()
    return maze
