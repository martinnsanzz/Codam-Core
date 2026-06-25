def handle_maze_input(key: str) -> str:
    if key == "R":
        return "regen"
    elif key == "C":
        return "change_color"
    elif key == "Q":
        return "quit"
    return "none"