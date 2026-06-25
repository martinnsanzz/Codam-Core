import curses

from .menu import Menu
from .windows_config import WINDOWS
from .game_loop import run_maze_loop


def window(stdscr: curses.window, state: str) -> str:
    config = WINDOWS[state]

    opt: Menu = Menu(stdscr, config["title"], config["options"])
    menu_window = opt.draw(config["h"], config["w"], config["pos"])

    while True:
        menu_window.refresh()
        
        key = opt.get_input()
        if key in config["keys"]:
            return config["keys"][key]


def maze_tui_window(stdscr: curses.window) -> str:
    config_opt = WINDOWS["maze_window"]["sub_options"]
    config_maze = WINDOWS["maze_window"]["sub_maze"]
    
    opt = Menu(stdscr, config_opt["title"], config_opt["options"])
    maze = Menu(stdscr, config_maze["title"], config_maze["options"])
    
    opt_window = opt.draw(config_opt["h"], config_opt["w"], config_opt["pos"])
    maze_window = maze.draw(config_maze["h"] + 1, config_maze["w"] + 1, config_maze["pos"])
    
    return run_maze_loop(stdscr, opt_window, maze_window, config_maze)
        

def main(stdscr: curses.window) -> None:
    curses.curs_set(0)

    states: list[str] = ["menu_window", "display_window",
                         "maze_options_window", "mlx", "quit"]
    cur_state = states[0]

    while cur_state != states[-1]:
        if cur_state == states[-2]:
            break
        elif cur_state == states[-3]:
            cur_state = maze_tui_window(stdscr)
            continue
        cur_state = window(stdscr, cur_state)