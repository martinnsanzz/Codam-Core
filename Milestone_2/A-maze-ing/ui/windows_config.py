"""
Window configuration and UI menu state manager.

Loads maze configuration and defines the layout, positioning,
and key bindings for all UI windows (menu, display selector, maze viewer).
"""

# Built-int modules
from typing import Any

# Local modules
from src.config_parser import config_parser
from src.utils import C, CustomError

# Load maze dimensions and settings from config file.
# On parse error, display failure message and exit immediately.
try:
    maze_config = config_parser("config.txt")
except CustomError as e:
    C().msg("F", str(e))
    quit()

# Window configuration map. Each key is a unique window state.
WINDOWS: dict[str, Any] = {
    "menu_window": {
        "title": "A-maze-ing",
        "options": [{"(C) Choose display": [3, 4],
                    "(Q) Quit": [5, 4]}],
        "h": 10, "w": 25,
        "pos": ["center"],
        "keys": {"C": "display_window", "Q": "quit"}
    },
    "display_window": {
        "title": "Choose display",
        "options": [{"(T) Terminal 'TUI'": [3, 4],
                     "(M) MLX": [4, 4],
                     "(Q) Quit": [7, 4]}],
        "h": 10, "w": 25,
        "pos": ["center"],
        "keys": {"T": "maze_options_window", "M": "mlx", "Q": "quit"}
    },
    "maze_window": {
        "sub_options": {
            "title": "Maze-menu",
            "options": [{"(R) Regenerate maze": [3, 2],
                         "(C) Change color": [4, 2],
                         "(Q) Quit": [6, 2]}],
            "h": 10, "w": 25,
            "pos": ["fixed", 0, 0],
            "keys": {"R": "regen", "C": "change_color", "Q": "quit"}
        },
        "sub_maze": {
            "title": "Maze",
            "options": [],
            "h": maze_config["HEIGHT"] + 1,
            "w": maze_config["WIDTH"] + 1,
            "pos": ["center"],
        }
    }
}
