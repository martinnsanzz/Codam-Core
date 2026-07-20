# Built-in modules
import curses
from typing import Any
from enum import Enum

# Local modules
from ..window import Window
from .windows_setup import WINDOWS
from .maze_loop import maze_loop
from ..state import State
from .input import handle_input


def start_window(stdscr: curses.window) -> State:
    """Display the start window and collect the user's menu selection.

    Draws the start-screen window, then blocks on key input until a
    valid ``State`` member is returned by ``handle_input``.

    Args:
        stdscr: The curses standard screen object.

    Returns:
        The ``State`` enum member selected by the user.
    """
    config = WINDOWS["start_window"]
    start_win = Window(stdscr, config)
    menu_window = start_win.draw_win(config)

    action = None
    while action not in State:
        action = handle_input(menu_window.getkey().upper())
    
    menu_window.refresh()
    return action


def main(stdscr: curses.window) -> None:
    """Run the maze application's main state-machine loop.

    Dispatches control to the appropriate handler for each state
    (start window, maze generation/play) until ``State.QUIT`` is
    reached. Tracks ``current_color`` across states so the active
    color scheme persists between window transitions.

    Args:
        stdscr: The curses standard screen object.
    """
    current_color = None

    curses.curs_set(0)
    cur_state = State.GEN_MAZE

    while cur_state != State.QUIT:
        if cur_state == State.START_WIN:
            cur_state = start_window(stdscr)
        elif cur_state == State.GEN_MAZE:
            stdscr.clear()
            cur_state, current_color = maze_loop(stdscr, current_color)
