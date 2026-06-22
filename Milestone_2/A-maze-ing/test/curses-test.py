#!/usr/bin/env python3

import curses
import time


def main(stdscr: curses.window) -> None:
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    Color1 = curses.color_pair(1)
    Color2 = curses.color_pair(2)
    Color3 = curses.color_pair(3)

    for i in range(100):
        stdscr.clear()
        color = Color1

        stdscr.border()
        if i % 2 == 0:
            color = Color2
        elif i % 3 == 0:
            color = Color3
        stdscr.addstr(10, 10, f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()

curses.wrapper(main)