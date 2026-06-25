from src.config_parser import config_parser
from src.utils import C, CustomError

try:
    maze_config = config_parser("config.txt")
except CustomError as e:
    C().msg("F", str(e))
    quit()


WINDOWS = {
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
        "sub_options" : {
            "title": "Maze-menu",
            "options": [{"(R) Regenerate maze": [3, 2],
                        "(C) Change color": [4, 2],
                        "(Q) Quit": [6, 2]}],
            "h": 10, "w": 25,
            "pos": ["fixed", 0, 0],
            "keys": {"R": "quit", "C": "quit", "Q": "quit"}
        },
        "sub_maze": {
            "title": "Maze",
            "h": maze_config["HEIGHT"], "w": maze_config["WIDTH"],
            "pos": ["center"],
            "options": []
        }
    }
}