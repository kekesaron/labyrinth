import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def load_map():
    maze_components=[]
    file = open("map.txt", "r")
    for row in file:
        for i in file:
            maze_components.append(i)
    file.close()
    return maze_components

def open_window(win,maze_components):
    win = curses.newwin(30, 90, 0, 0)  # Init window object
    curses.noecho()             # Disable default printing of inputs
    curses.curs_set(0)          # Hiding cursor visibility (https://docs.python.org/2/library/curses.html#curses.curs_set)
    win.keypad(1)               # enable processing of functional keys by curses (ex. arrow keys)              # set a border for the window
    win.nodelay(1)
    y=1
    x=1
    win.addch(y,x, 'O')
    for coord_y in range(0,20):
        for coord_x in range(0,70):
                win.addch(coord_y,coord_x,maze_components[coord_y-1][coord_x])
    while True:
        event = win.getch()
        if event == ord ("q"):
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
