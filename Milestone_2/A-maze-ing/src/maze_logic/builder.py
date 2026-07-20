# Local Modules
from src import MazeConfig, Gen_Kruskal, DFS
from .maze import Maze

def select_gen_algorithm(maze_config: MazeConfig) -> Maze:
    algorithm_name: str = maze_config.algorithm

    if algorithm_name == "kruskal":
        maze = build_kruskal_maze(maze_config)
    elif algorithm_name == "dfs":
        maze = build_dfs_maze(maze_config)
    
    # if not maze_config.perfect:
    #     maze = build_imperfect_maze(maze)
    return maze

def build_kruskal_maze(maze_config: MazeConfig) -> Maze:
    maze = Maze(maze_config)
    builder = Gen_Kruskal(maze)
    builder.construct()
    return maze

def build_dfs_maze(maze_config: MazeConfig) -> Maze:
    maze = Maze(maze_config)
    builder = DFS(maze)
    builder.construct()
    return maze

# def build_imperfect_maze(maze: Maze) -> Maze:
#     imperfect = ImperfectMaze(maze)
#     imperfect.construct()

#     return maze