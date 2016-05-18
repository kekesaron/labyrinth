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
    y=1
    x=1
    win.addch(y,x, 'O')
    win.addstr(0,0,string)
    while True:
        event = win.getch()
        if (event == ord("q")):
            break
        elif event == curses.KEY_RIGHT :
            win.addch(y,x, ' ')
            win.addch(y,x+1, 'O')
            x=x+1
            win.refresh()
        elif event == curses.KEY_LEFT :
            win.addch(y,x, ' ')
            win.addch(y,x-1, 'O')
            x=x-1
            win.refresh()
        elif event == curses.KEY_DOWN :
            win.addch(y,x, ' ')
            win.addch(y+1,x, 'O')
            y=y+1
            win.refresh()
        elif event == curses.KEY_UP :
            win.addch(y,x, ' ')
            win.addch(y-1,x, 'O')
            y=y-1
            win.refresh()


    curses.endwin()
win= curses.initscr()
load_map()
open_window(win, load_map())
