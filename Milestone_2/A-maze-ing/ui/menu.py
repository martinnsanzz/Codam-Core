# Built-in modules
import curses
from typing import Any

# Local modules
from .windows_config import WINDOWS
from src.utils import CustomError

class Menu():
    def __init__(self, stdscr: curses.window, title: str,
                 options: list[dict[str, list[int]]] = []) -> None:
        self.stdscr = stdscr
        self.title = title
        self.options = options

    def draw(self, menu_h: int, menu_w: int, pos: list[Any]) -> curses.window:
        maze_config = WINDOWS["maze_window"]["sub_maze"]
        self.stdscr.refresh()
        term_h, term_w = self.stdscr.getmaxyx()

        if pos[0] == "center":
            y = (term_h - menu_h) // 2
            x = (term_w - menu_w) // 2
        elif pos[0] == "top-maze":
            y = ((term_h - maze_config["h"]) // 2) - menu_h
            x = (term_w - menu_w) // 2

        menu = curses.newwin(menu_h, menu_w, y, x)

        if not self.title == "Maze":
            menu.box()
            menu.addstr(0, 0, self.title, curses.A_BOLD)

        for _ in self.options:
            for key, value in _.items():
                menu.addstr(value[0], value[1], key)

        return menu


    def get_input(self) -> str:
        return self.stdscr.getkey().upper()
