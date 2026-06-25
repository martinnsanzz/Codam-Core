import curses

from src.maze.maze_gen import generate_maze, change_color, draw_maze
from src.utils import CustomError, C
from src.config_parser import config_parser
from input_handler import handle_maze_input


def _handle_regen(maze_window, config):
    try:
        fresh_config = config_parser("config.txt")
        return generate_maze(fresh_config["HEIGHT"], fresh_config["WIDTH"]), ""
    except CustomError:
        return current_maze, "Config Error"

def _display_error(window, message):
    if message:
        window.addstr(8, 6, message, curses.color_pair(10))
    else:
        window.addstr(8, 6, "            ")


def run_maze_loop(stdscr, opt_window, maze_window, opt_menu, config) -> str:
    current_maze = generate_maze(config["h"], config["w"])
    current_color = change_color()
    error_message = ""
    
    while True:
        draw_maze(maze_window, current_maze, current_color)
        _display_error(opt_window, error_message)
        opt_window.refresh()
        
        key = opt_menu.get_input()
        action = handle_maze_input(key)
        
        if action == "regen":
            current_maze, error_message = _handle_regen(maze_window, config)
        elif action == "change_color":
            current_color = change_color()
        elif action == "quit":
            return "quit"
        
