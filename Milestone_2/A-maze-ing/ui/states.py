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
from .tui import run_maze_loop


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


# Display the maze game loop with an overlay menu.

# Renders two overlapping windows: the main maze display and a floating
# options menu (regen, color, quit). Delegates to run_maze_loop for game
# logic and returns the next state when user exits.
def maze_tui_window(stdscr: curses.window) -> str:

    config_opt = WINDOWS["maze_window"]["sub_options"]
    config_maze = WINDOWS["maze_window"]["sub_maze"]

    opt = Menu(stdscr, config_opt["title"], config_opt["options"])
    maze = Menu(stdscr, config_maze["title"], config_maze["options"])

    opt_window = opt.draw(config_opt["h"], config_opt["w"], config_opt["pos"])
    maze_window = maze.draw(config_maze["h"], config_maze["w"],
                            config_maze["pos"])

    return run_maze_loop(stdscr, opt_window, maze_window, config_maze)


# Entry point for the TUI application. Runs the state machine loop.
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
