# Built-in modules
import curses
import time

# Local modules
from .classes import Flag, Pixel

def draw_maze(maze_window: curses.window, maze_grid: list[list[Pixel]],
              color_count: int, color: int) -> None:
    flag: Flag
    # print(color, file=sys.stderr)
    colors = set()
    for row in range(len(maze_grid)):
        for col in range(len(maze_grid[row])):
            flag = maze_grid[row][col].read()
            try:
                cell_color = ((flag.value + color - 1) % color_count) + 1
                colors.add(cell_color)
                maze_window.addstr(row, col * 2, "██", curses.color_pair(cell_color))
            except IndexError:
                raise IndexError(f"{flag} - {flag.value} - {color} = ERROR")
    # print(colors, file=sys.stderr)
    maze_window.refresh()

def draw_solution(maze_window: curses.window, steps: list[tuple[int, int]],
              color_count: int, color: int) -> None:
    for row, col in steps:
        cell_color = (Flag.SOLUTION.value + color) % color_count
        maze_window.addstr(row, col * 2, "██", curses.color_pair(cell_color))
        maze_window.refresh()
        #time.sleep(0.05)

