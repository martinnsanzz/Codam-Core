"""
Terminal UI (TUI) state machine and window controller.

Manages menu navigation and display using curses. Routes between different
UI windows based on user input and current state.
"""

# Built-in modules
import curses
from typing import Any

# Local modules
from .menu import Menu
from .windows_config import WINDOWS
from .tui.game_loop import run_maze_loop, maze_opt_window, maze_window, palette_window



# Display a generic menu window and return the next state based on key input.

# Loads window config from WINDOWS, renders the menu, and loops until user
# presses a mapped key. Returns the associated next state from
# config["keys"].
def window(stdscr: curses.window, state: str) -> Any:

    config = WINDOWS[state]
    opt = Menu(stdscr, config["title"], config["options"])
    menu_window = opt.draw(config["h"], config["w"], config["pos"])

    while True:
        menu_window.refresh()
        key = opt.get_input()
        if key in config["keys"]:
            return config["keys"][key]


# Execute the maze game with transparent window resizing.
# Runs the main maze loop. If config dimensions change during gameplay,
# clears the screen and rebuilds windows, then restarts the loop with
# the same color scheme. Returns only when user quits.
def maze_tui_window(stdscr: curses.window) -> str:
    current_color = None

    while True:
        opt_win = maze_opt_window(stdscr)
        maze_win = maze_window(stdscr)
        pal_win = palette_window(stdscr)
        
        result, current_color = run_maze_loop(stdscr, opt_win, maze_win, pal_win,
                              WINDOWS["maze_window"]["sub_maze"], current_color)
        
        if result == "quit":
            return result
        if result == "resize":
            stdscr.clear()
            continue


# Entry point for the TUI application. Runs the state machine loop.
# Initializes curses (hides cursor), starts at "maze_options_window", and
# transitions between states until "quit" is returned.
def main(stdscr: curses.window) -> None:

    windows_list = ["menu_window", "display_window", "maze_options_window"]

    curses.curs_set(0)
    cur_state = windows_list[2]

    while cur_state != "quit":
        if cur_state == "mlx":
            break
        elif cur_state == "maze_options_window":
            cur_state = maze_tui_window(stdscr)
        else:
            cur_state = window(stdscr, cur_state)
