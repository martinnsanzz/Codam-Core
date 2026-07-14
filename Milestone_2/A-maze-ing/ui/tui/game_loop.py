# Built-in modules
import curses
from typing import Any

# Local modules
from src.maze.maze_gen import generate_maze, change_color, draw_maze
from src.utils import CustomError
from ui.windows_config import WINDOWS
from ui.menu import Menu


def run_maze_loop(stdscr: curses.window, opt_window: curses.window,
                  maze_window: curses.window, config_maze: dict[str, Any],
                  current_color: tuple | None = None) -> tuple[str, tuple]:
    current_maze = generate_maze(config_maze["h"] - 1, config_maze["w"] - 1)
    if current_color is None:
        current_color = change_color()

    while True:
        draw_maze(maze_window, current_maze, current_color)
        opt_window.refresh()

        key = stdscr.getkey().upper()
        action = handle_maze_input(key)

        if action == "regen":
            # maze_result, status = regenerate_or_resize(config_maze)
            # if status == "resize":
            #     return "resize", current_color
            # current_maze = maze_result
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

    try: 
        maze_window = maze.draw(config_maze["h"], config_maze["w"],
                        config_maze["pos"])
    except BaseException:
        raise CustomError("Screen does not fit maze. "
                              "Reduce width in 'config.txt'")

    return maze_window


# def regenerate_or_resize(config_maze: dict[str, Any]) -> tuple[list[list[int]] | None, str]:
#     maze_config = config_parser("config.txt")
#     new_h = maze_config["HEIGHT"] + 1
#     new_w = maze_config["WIDTH"] + 1
    
#     # Check if dimensions changed; if so, update WINDOWS and signal resize
#     if new_h != config_maze["h"] or new_w != config_maze["w"]:
#         WINDOWS["maze_window"]["sub_maze"]["h"] = new_h
#         WINDOWS["maze_window"]["sub_maze"]["w"] = new_w
#         return None, "resize"
    
#     # Dimensions unchanged; regenerate maze with current size
#     current_maze = generate_maze(maze_config["HEIGHT"], maze_config["WIDTH"])
#     return current_maze, "regen"


# Map keyboard input to game action string.
def handle_maze_input(key: str) -> str:
    actions = {
        "R": "regen",
        "C": "change_color",
        "Q": "quit"
    }
    return actions.get(key, "")
