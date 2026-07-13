#!/usr/bin/env python3

def render_cell(value) -> list[list[str]]:
    grid = [[" " for _ in range(3)] for _ in range(3)]

    # Extract wall presence using bitwise AND
    has_top    = value & 1
    has_right  = value & 2
    has_bottom = value & 4
    has_left   = value & 8

    # Apply solid block walls based on the active bits
    if has_top:
        grid[0][0] = grid[0][1] = grid[0][2] = "█"
    if has_bottom:
        grid[2][0] = grid[2][1] = grid[2][2] = "█"
    if has_left:
        grid[0][0] = grid[1][0] = grid[2][0] = "█"
    if has_right:
        grid[0][2] = grid[1][2] = grid[2][2] = "█"
    
    return grid

def print_cell(value):
    # Print the top rows of all cells, then middle rows, then bottom rows
    cell = render_cell(value)

    for row_idx in range(3):
        for col_inx in range(3):
            print(cell[row_idx][col_inx], end="")
        print()


if __name__ == "__main__":
    print_cell(9)