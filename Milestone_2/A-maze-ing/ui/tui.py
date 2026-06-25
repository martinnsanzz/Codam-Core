#!/usr/bin/env python3

import curses
from random import randint
from src.config_parser import config_parser
from src.maze.maze_gen import generate_maze, change_color, draw_maze


WINDOWS = {
    "menu_window": {
        "title": "A-maze-ing",
        "options": [{"(C) Choose display": [3, 4],
                     "(Q) Quit": [5, 4]}],
        "h": 10, "w": 25,
        "keys": {"C": "display_window", "Q": "quit"}
    },
    "display_window": {
        "title": "Choose display",
        "options": [{"(T) Terminal 'TUI'": [3, 4],
                     "(M) MLX": [4, 4],
                     "(Q) Quit": [7, 4]}],
        "h": 10, "w": 25,
        "keys": {"T": "maze_options_window", "M": "mlx", "Q": "quit"}
    },
    "maze_window": {
        "sub_options" : {
            "title": "Maze-menu",
            "options": [{"(R) Regenerate maze": [3, 2],
                         "(C) Change color": [4, 2],
                         "(Q) Quit": [6, 2]}],
            "h": 10, "w": 25,
            "keys": {"R": "quit", "C": "quit", "Q": "quit"}
        },
        "sub_maze": {
            "title": "Maze",
            "h": 15, "w": 30,
            "options": []
        }
    }
}


class Menu():
    def __init__(self, stdscr: curses.window, title: str,
                       options: list[dict[str, list[int]]] = []) -> None:
        self.stdscr = stdscr
        self.title = title
        self.options = options

    def draw(self, menu_h, menu_w, pad_y = 0, pad_x = 0) -> curses.window:
        self.stdscr.clear()
        self.stdscr.refresh()
        term_h, term_w = self.stdscr.getmaxyx()

        if self.title != "Maze-menu":
            y = ((term_h - menu_h) // 2) + pad_y
            x = ((term_w - menu_w) // 2) + pad_x
        else:
            y = 0
            x = 0
        
        menu = curses.newwin(menu_h, menu_w, y, x)
        menu.box()
        menu.addstr(0, 0, self.title, curses.A_BOLD)

        for x in self.options:
            for key, value in x.items():
                menu.addstr(value[0], value[1], key)
        return menu

    def get_input(self) -> str:
        return self.stdscr.getkey().upper()



def window(stdscr: curses.window, state: str) -> str:
    config = WINDOWS[state]

    opt: Menu = Menu(stdscr, config["title"], config["options"])
    menu_window = opt.draw(config["h"], config["w"])

    while True:
        menu_window.refresh()
        
        key = opt.get_input()
        if key in config["keys"]:
            return config["keys"][key]


def maze_tui_window(stdscr: curses.window) -> str:
    maze_config = config_parser("config.txt")
    current_color = change_color()

    config_opt = WINDOWS["maze_window"]["sub_options"]
    config_maze = WINDOWS["maze_window"]["sub_maze"]
 
    opt: Menu = Menu(stdscr, config_opt["title"], config_opt["options"])
    maze: Menu = Menu(stdscr, config_maze["title"], config_maze["options"])

    opt_window = opt.draw(config_opt["h"], config_opt["w"])
    try:
        maze_window = maze.draw(maze_config["HEIGHT"] + 1, maze_config["WIDTH"] + 1)
        current_maze = generate_maze(maze_config)
    except Exception:
        opt_window.addstr(8, 2, "Error")

    while True:
        draw_maze(maze_window, current_maze, current_color)
        maze_config = config_parser("config.txt")
        opt_window.refresh()

        key = opt.get_input()
        if key == "R":
            current_maze = generate_maze(maze_config)
        elif key == "C":
            current_color = change_color()
        elif key == "Q":
            return "quit"


def main(stdscr: curses.window) -> None:
    curses.curs_set(0)

    states: list[str] = ["menu_window", "display_window",
                         "maze_options_window", "mlx", "quit"]
    cur_state = states[2]

    while cur_state != states[-1]:
        if cur_state == states[-2]:
            break
        elif cur_state == states[-3]:
            cur_state = maze_tui_window(stdscr)
            continue
        cur_state = window(stdscr, cur_state)
