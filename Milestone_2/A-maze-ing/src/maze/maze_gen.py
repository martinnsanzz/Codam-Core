#!/usr/bin/env python3

from random import randint
import curses


COLORS = [
    curses.COLOR_WHITE,
    curses.COLOR_RED,
    curses.COLOR_GREEN,
    curses.COLOR_MAGENTA,
    curses.COLOR_BLUE
]

def generate_maze(maze_config: dict) -> list[str, str]:
    list_2d = []

    for _ in range(1, maze_config["HEIGHT"]):
        letter = randint(0, 25)
        list_1d = []
        for _ in range(1, maze_config["WIDTH"]):
            list_1d.append(chr(letter + 65))
            letter += 1
            if letter == 26:
                letter = 0
        list_2d.append(list_1d)
    return list_2d

def draw_maze(maze_window: curses.window, maze: list,
              color: int) -> None:
    for i in range(1, len(maze)):
        for j in range(1, len(maze[i])):
            maze_window.addstr(i, j, maze[i - 1][j - 1], color)
            maze_window.refresh()

def change_color() -> int:
    current = 0
    
    curses.init_pair(current + 1, COLORS[current], curses.COLOR_BLACK)
    color = curses.color_pair(current + 1)

    def count() -> int:
        nonlocal current
        current += 1
        
    return color