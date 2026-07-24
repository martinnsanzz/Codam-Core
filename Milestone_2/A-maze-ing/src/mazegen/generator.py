# Build-in modules
from random import Random

# Local modules
from .classes import Maze
from .solve_algorithms import Maze_Solve_Perfect
from .gen_algorithms import build_kruskal_maze, build_dfs_maze


class MazeGenerator():
    """Build and solve mazes using a configurable generation algorithm.

    Instantiate with the maze dimensions and the desired generation
    algorithm, then call `generate()` to produce a `Maze` and `solve()`
    to get a string with the directions to solve the maze and a 
    list of tuples with the cordinates of each move.

    Attributes:
        _width (int): Number of columns in the generated maze.
        _height (int): Number of rows in the generated maze.
        _algorithm (str): Generation algorithm identifier
            (``"kruskal"`` or ``"dfs"``).
        _perfect (bool): Whether the maze is generated as "perfect"
            (exactly one path between any two cells, no loops).
        _rng (Random): Seeded random number generator used for
            deterministic or randomized generation.
    
    Notes:
        If the provided algorithm isnt on the supported list it will provide a maze
        with all walls up
    """
    def __init__(self, width: int, height: int, algorithm: str, perfect: bool,
                 seed: int | None = None) -> None:
        """Initialize generator parameters.

        Args:
            width: Number of columns in the maze.
            height: Number of rows in the maze.
            algorithm: Generation algorithm to use. Supported values
                are ``"kruskal"`` and ``"dfs"``.
            perfect: If True, generate a perfect maze (no loops).
            seed: Seed for the random number generator. If None, the
                generator is seeded non-deterministically.
        """
        self._width = width
        self._height = height
        self._algorithm = algorithm
        self._perfect = perfect
        self._rng = Random(seed)

    def generate(self) -> Maze:
        """Generate a maze using the configured algorithm.

        Returns:
            Maze: A new maze built with the configured algorithm. If
            `algorithm` is not `"kruskal"` or `"dfs"`, an empty,
            unmodified `Maze` is returned (no passages carved).

        Notes:
            Once the maze is greated use method .get_print_string() to print
            the maze to the terminal.
        """
        if self._width < 2 or self._height < 2:
            raise RuntimeError("Size of maze cant be smaller than 2x2. "
                               "Increase the size of the maze")
        
        maze = Maze(self._width, self._height, self._perfect)

        
        if self._algorithm == "kruskal":
            build_kruskal_maze(maze, self._rng)
        elif self._algorithm == "dfs":
            build_dfs_maze(maze, self._rng)
        return maze

    
    def solve(self, maze: Maze, entry: tuple[int, int], 
              exit: tuple[int, int]) -> tuple[str, list[tuple[int, int]]]:
        """Solve a maze between two points.

        Args:
            maze: Maze instance to solve.
            entry: (row, col) coordinate of the starting cell. Min value (0, 0)
            exit: (row, col) coordinate of the target cell. 
                  Max value (width - 1, height - 1)

        Returns:
            tuple[str, list[tuple[int, int]]]: Solution identifier and
            the ordered list of coordinates from `entry` to `exit`.

        Raises:
            If entry and exit aren't within the maze bounds or if they're the same
        """
        if self._perfect:
            perfect_solver = Maze_Solve_Perfect()

            try:
                solution = perfect_solver.solve(maze, entry, exit)
                return solution, perfect_solver.steps
            except BaseException:
                raise RuntimeError("Entry or exit values aren't within the maze bounds or "
                                   "are equal !! This triggers and error fix it !!")
