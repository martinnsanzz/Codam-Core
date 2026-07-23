# Build-in modules
from random import Random

# Local modules
from .classes import Maze
from .solve_algorithms import Maze_Solve_Perfect
from .gen_algorithms import build_kruskal_maze, build_dfs_maze


class MazeGenerator():
    def __init__(self, width: int, height: int, algorithm: str, perfect: bool,
                 seed: int | None = None) -> None:
        self._width = width
        self._height = height
        self._algorithm = algorithm
        self._perfect = perfect
        self._rng = Random(seed)

    def generate(self) -> Maze:
        maze = Maze(self._width, self._height, self._perfect)

        if self._algorithm == "kruskal":
            build_kruskal_maze(maze, self._rng)
        elif self._algorithm == "dfs":
            build_dfs_maze(maze, self._rng)
        return maze
    
    def solve(self, maze: Maze, entry: tuple[int, int], 
              exit: tuple[int, int]) -> tuple[str, list[tuple[int, int]]]:

        if self._perfect:
            perfect_solver = Maze_Solve_Perfect()
            solution = perfect_solver.solve(maze, entry, exit)
            return solution, perfect_solver.steps
