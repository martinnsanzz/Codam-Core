# Built-in modules
import curses

COLORS = [
    curses.COLOR_WHITE,
    curses.COLOR_RED,
    curses.COLOR_GREEN,
    curses.COLOR_MAGENTA,
    curses.COLOR_BLUE
]

current_color_index = 0


def draw_maze(maze_window: curses.window, maze_grid: list[list[str]],
              color: int) -> None:
    for x in range(len(maze_grid)):
        for y in range(len(maze_grid[x])):
            char = maze_grid[x][y]
            maze_window.addstr(x, y * 2, char, color)

    maze_window.refresh()


def change_color() -> int:
    global current_color_index
    curses.init_pair(current_color_index + 1, COLORS[current_color_index],
                     curses.COLOR_BLACK)
    color = curses.color_pair(current_color_index + 1)
    current_color_index = (current_color_index + 1) % len(COLORS)
    return color