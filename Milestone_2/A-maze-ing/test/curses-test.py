#!/usr/bin/env python3

import curses
import time


def main(stdscr: curses.window) -> None:
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    Color1 = curses.color_pair(1)
    Color2 = curses.color_pair(2)
    Color3 = curses.color_pair(3)
    Color4 = curses.color_pair(4)

    color = Color1
    stdscr.clear()
    x, y = 10, 10
    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            x -= 1
            color = Color1
        elif key == "KEY_RIGHT":
            x +=1
            color = Color2
        elif key == "KEY_UP":
            y -= 1
            color = Color3
        elif key == "KEY_DOWN":
            y += 1
            color = Color4
        elif key == "KEY_ENTER":
            stdscr.addstr(y, x, "Hello", color)
            exit
        stdscr.clear()
        stdscr.addstr(y, x, "0", color)
        stdscr.refresh()
curses.wrapper(main)