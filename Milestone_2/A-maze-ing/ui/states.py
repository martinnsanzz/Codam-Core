# Built-in modules
import curses
from typing import Any

# Local modules
from .menu import Menu
from .windows_config import WINDOWS
from .tui.game_loop import run_maze_loop, maze_opt_window, maze_window


def window(stdscr: curses.window, state: str) -> Any:
    config = WINDOWS[state]
    opt = Menu(stdscr, config["title"], config["options"])
    menu_window = opt.draw(config["h"], config["w"], config["pos"])

    while True:
        menu_window.refresh()
        key = opt.get_input()
        if key in config["keys"]:
            return config["keys"][key]


def maze_tui_window(stdscr: curses.window) -> str:
    current_color = None

    while True:
        opt_win = maze_opt_window(stdscr)
        maze_win = maze_window(stdscr)
        
        result, current_color = run_maze_loop(stdscr, opt_win, maze_win, current_color)
        
        if result == "quit":
            return result
        if result == "resize":
            stdscr.clear()
            continue


def main(stdscr: curses.window) -> None:

    windows_list = ["menu_window", "display_window", "maze_options_window"]

    curses.curs_set(0)
    cur_state = windows_list[2]

    while cur_state != "quit":
        stdscr.clear()
        if cur_state == "mlx":
            break
        elif cur_state == "maze_options_window":
            cur_state = maze_tui_window(stdscr)
        else:
            cur_state = window(stdscr, cur_state)
