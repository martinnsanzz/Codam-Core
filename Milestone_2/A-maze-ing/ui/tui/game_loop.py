# Built-in modules
import curses
from typing import Any

# Local modules
from src.maze_logic.maze_display import change_color, draw_maze
from src.maze_logic.maze import Maze
from src import load_maze_config, MazeConfig
from src.utils import CustomError
from ui.windows_config import WINDOWS
from ui.menu import Menu


def run_maze_loop(stdscr: curses.window, opt_window: curses.window,
                  maze_window: curses.window,
                  current_color: tuple | None = None) -> tuple[str, tuple]:
    maze_config = load_maze_config()
    maze = Maze(maze_config)

    maze_grid = maze.get_maze()

    if current_color is None:
        current_color = change_color()

    while True:
        draw_maze(maze_window, maze_grid, current_color)
        opt_window.refresh()

        key = stdscr.getkey().upper()
        action = handle_maze_input(key)

        if action == "regen":
            maze_result, status = regenerate_or_resize(maze_config, maze)
            if status == "resize":
                return "resize", current_color
            maze_grid = maze_result
            continue
        elif action == "change_color":
            current_color = change_color()
        elif action == "quit":
            return "quit", current_color


def maze_opt_window(stdscr: curses.window) -> curses.window:
    config_opt = WINDOWS["maze_window"]["sub_options"]

    opt = Menu(stdscr, config_opt["title"], config_opt["options"])

    try: 
        opt_window = opt.draw(config_opt["h"], config_opt["w"], config_opt["pos"])
    except BaseException:
        raise CustomError("Maze option menu outside of screen. "
                                "Reduce height in 'config.txt'")

    return opt_window



def maze_window(stdscr: curses.window) -> curses.window:
    config_maze = WINDOWS["maze_window"]["sub_maze"]
    maze = Menu(stdscr, config_maze["title"], config_maze["options"])
    return maze.draw(config_maze["h"], config_maze["w"], config_maze["pos"])


def regenerate_or_resize(old_config: MazeConfig, maze: Maze) -> tuple[list[list[int]] | None, str]:
    new_config = load_maze_config()
    new_h = 2 * new_config.height + 1
    new_w = 2 * (2 * new_config.width + 1) + 1

    # Check if dimensions changed; if so, update WINDOWS and signal resize
    if new_h != old_config.height or new_w != old_config.width:
        WINDOWS["maze_window"]["sub_maze"]["h"] = new_h
        WINDOWS["maze_window"]["sub_maze"]["w"] = new_w
        return None, "resize"
    
    # Dimensions unchanged; regenerate maze with current size
    maze_grid = maze.get_maze()

    return maze_grid, "regen"


# Map keyboard input to game action string.
def handle_maze_input(key: str) -> str:
    actions = {
        "R": "regen",
        "C": "change_color",
        "Q": "quit"
    }
    return actions.get(key, "")
