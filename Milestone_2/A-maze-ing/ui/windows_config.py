# Built-int modules
from typing import Any

# Local modules
from src import load_maze_config, CustomError, C
from pydantic import ValidationError

# Load maze dimensions and settings from config file.
# On parse error, display failure message and exit immediately.
try:
    maze_config = load_maze_config()
except (ValidationError, CustomError) as e:
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
            "options": [{"(R) Regenerate maze": [2, 3],
                         "(C) Change color": [3, 3],
                         "(Q) Quit": [3, 25]}],
            "h": 6,
            "w": 50,
            "pos": ["top-maze"],
            "keys": {"R": "regen", "C": "change_color", "Q": "quit"}
        },
        "sub_maze": {
            "title": "Maze",
            "options": [],
            "h": maze_config.height,
            "w": maze_config.width,
            "pos": ["center"],
        }
    }
}
