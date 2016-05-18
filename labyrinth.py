import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def load_map():
    fo = open("map.txt", "r+")
    string=fo.read()
    fo.close()
    return string
def open_window(win,string):
    win = curses.newwin(20, 80, 0, 0)  # Init window object
    curses.noecho()             # Disable default printing of inputs
    curses.curs_set(0)          # Hiding cursor visibility (https://docs.python.org/2/library/curses.html#curses.curs_set)
    win.keypad(1)               # enable processing of functional keys by curses (ex. arrow keys)              # set a border for the window
    win.nodelay(1)
    while True:
        win.addstr(0,0,string)
        event=win.getch()
        if (event == ord('q')):
            break
    curses.endwin()
win= curses.initscr()
load_map()
open_window(win, load_map())
