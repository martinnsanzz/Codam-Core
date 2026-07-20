# Built-in modules
import curses

# Local modules
from src import load_maze_config, select_gen_algorithm, MazeConfig
from src.maze_logic.maze_display import change_color, draw_maze
from .windows_setup import WINDOWS
from ..window import MazeWindow
from .input import handle_input
from ..state import State


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

        if action == State.REGEN:
            new_config = load_maze_config()

            action = resize_maze(maze_config)
            if action == State.REGEN:
                maze_config = new_config
                maze_grid = select_gen_algorithm(maze_config).get_maze()
            else:
                return action, current_color
        elif action == State.CHANGE_COLOR:
            current_color = change_color()
        elif action == State.QUIT:
            return State.QUIT, current_color


def resize_maze(old_config : MazeConfig) -> State:
    """Detect a config change and update window dimensions if needed.

    Reloads the maze configuration and compares it against the given
    one. If they differ, resizes the maze sub-window's height/width in
    ``WINDOWS`` to match the new dimensions.

    Args:
        old_config (MazeConfig): The maze configuration currently in use.

    Returns:
        ``State.GEN_MAZE`` if the configuration changed and the window
        was resized, otherwise ``State.REGEN``.
    """
    new_config = load_maze_config()

    if (old_config != new_config):
        WINDOWS["maze_window"]["sub_maze"]["h"] = 2 * new_config.height + 1
        WINDOWS["maze_window"]["sub_maze"]["w"] = 2 * (2 * new_config.width + 1) + 1
        return State.GEN_MAZE
    return State.REGEN