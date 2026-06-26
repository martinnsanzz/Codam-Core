"""
Maze game loop and input handler.

Manages the main gameplay loop: maze generation, rendering, user input
capture, and state updates (regen, color change, exit). Runs continuously
until user quits or triggers a state transition.
"""

# Built-in modules
import curses
from typing import Any

# Local modules
from src.maze.maze_gen import generate_maze, change_color, draw_maze
from src.config_parser import config_parser


# Execute the main maze game loop with rendering and input handling.
# Generates an initial maze, then enters an infinite loop: redraw maze,
# capture keyboard input, dispatch action (regenerate, color change, quit).
# Redraws on every frame. Returns only when user presses 'Q' (quit).
def run_maze_loop(stdscr: curses.window, opt_window: curses.window,
                  maze_window: curses.window,
                  config_maze: dict[str, Any]) -> str:
    current_maze = generate_maze(config_maze["h"] - 1, config_maze["w"] - 1)
    current_color = change_color()

    while True:
        draw_maze(maze_window, current_maze, current_color)
        opt_window.refresh()

        key = stdscr.getkey().upper()
        action = handle_maze_input(key)

        if action == "regen":
            maze_config = config_parser("config.txt")
            current_maze = generate_maze(maze_config["HEIGHT"],
                                         maze_config["WIDTH"])
        elif action == "change_color":
            current_color = change_color()
        elif action == "quit":
            return "quit"


# Map keyboard input to game action string.
def handle_maze_input(key: str) -> str:
    actions = {
        "R": "regen",
        "C": "change_color",
        "Q": "quit"
    }
    return actions.get(key, "")
