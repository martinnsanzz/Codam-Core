# Built-in modules
import curses

# Local modules
from src import load_maze_config, select_gen_algorithm, MazeConfig, \
                draw_maze, change_color
from ..window_class import MazeWindow
from ..state import State
from ..windows_config import WINDOWS


def maze_loop(stdscr: curses.window, current_color: int | None) \
                -> tuple[State, int | None]:
    """Run the maze display and interaction loop until exit or regen.

    Loads the maze configuration, builds the maze grid, and repeatedly
    draws and refreshes the maze window while dispatching user input
    to color-change, regenerate, or quit actions.

    Args:
        stdscr (curses.window): The curses standard screen object.
        current_color (int | None): The active color scheme index, or ``None`` if
            no color has been set yet (triggers ``change_color()``).

    Returns:
        A tuple of ``(action, current_color)`` where ``action`` is the
        resulting ``State`` (e.g. ``State.QUIT`` or the value from
        ``resize_maze``) and ``current_color`` is the color scheme
        index to carry into the next state.
    """
    maze_config = load_maze_config()
    maze_window_obj = MazeWindow(stdscr)
    
    stdscr.refresh()
    maze_win = maze_window_obj.maze_win
    maze_grid = select_gen_algorithm(maze_config).get_maze()


    if current_color is None:
        current_color = change_color()

    while True:
        draw_maze(maze_win, maze_grid, current_color)
        maze_window_obj.refresh_all()
        action = handle_input(stdscr.getkey().upper())

        if action == State.GEN_MAZE:
            action, maze_config = regen_maze(maze_config)
            maze_grid = select_gen_algorithm(maze_config).get_maze()
            return action, current_color
        elif action == State.CHANGE_COLOR:
            current_color = change_color()
        elif action == State.QUIT:
            return State.QUIT, current_color


def regen_maze(old_config : MazeConfig) -> tuple[State, MazeConfig]:
    """Detect a config change and update window dimensions if needed.

    Reloads the maze configuration and compares it against the given
    one. If they differ, resizes the maze sub-window's height/width in
    ``WINDOWS`` to match the new dimensions.

    Args:
        old_config (MazeConfig): The maze configuration currently in use.

    Returns:
        A tuple of ``State.GEN_MAZE`` to generate a new maze and 
        ``new_config`` to get the new configuration of the maze
    """
    new_config = load_maze_config()

    if (old_config != new_config):
        WINDOWS["maze_window"]["sub_maze"]["h"] = 2 * new_config.height + 1
        WINDOWS["maze_window"]["sub_maze"]["w"] = 2 * (2 * new_config.width + 1) + 1
    return State.GEN_MAZE, new_config


def handle_input(key: str) -> int:
    """Map an uppercase input key to its corresponding state action."""
    actions = {
        "G": State.GEN_MAZE,
        "R": State.GEN_MAZE,
        "C": State.CHANGE_COLOR,
        "Q": State.QUIT}
    return actions.get(key, "")