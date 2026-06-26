# Built-in modules
from random import randint
import curses

COLORS = [
    curses.COLOR_WHITE,
    curses.COLOR_RED,
    curses.COLOR_GREEN,
    curses.COLOR_MAGENTA,
    curses.COLOR_BLUE
]

current_color_index = 0


def generate_maze(maze_h: int, maze_w: int) -> list[list[str]]:
    list_2d = []

    for _ in range(0, maze_h):
        letter = randint(0, 25)
        list_1d = []
        for _ in range(0, maze_w):
            list_1d.append(chr(letter + 65))
            letter += 1
            if letter == 26:
                letter = 0
        list_2d.append(list_1d)
    return list_2d


def draw_maze(maze_window: curses.window, maze: list[list[str]],
              color: int) -> None:
    for i in range(1, len(maze)):
        for j in range(1, len(maze[i])):
            maze_window.addstr(i, j, maze[i - 1][j - 1], color)

    maze_window.refresh()


def change_color() -> int:
    global current_color_index
    curses.init_pair(current_color_index + 1, COLORS[current_color_index],
                     curses.COLOR_BLACK)
    color = curses.color_pair(current_color_index + 1)
    current_color_index = (current_color_index + 1) % len(COLORS)
    return color
