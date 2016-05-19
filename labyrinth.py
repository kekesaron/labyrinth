import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

coord_x=1
coord_y=1

def init_coord():
    global coord_x
    coord_x=1
    global coord_y
    coord_y=1

def show_map(maze_components,win):
    global coord_x
    global coord_y
    init_coord()
    win.addch(coord_y,coord_x, 'O')
    for coord_y in range(0,20):
        for coord_x in range(0,70):
                win.addch(coord_y,coord_x,maze_components[coord_y-1][coord_x])

def load_map():
    maze_components=[]
    file = open("map.txt", "r")
    for row in file:
        for i in file:
            maze_components.append(i)
    file.close()
    return maze_components

def open_window(win,maze_components):
    win = curses.newwin(40, 100, 0, 0)  # Init window object
    curses.noecho()             # Disable default printing of inputs
    curses.curs_set(0)          # Hiding cursor visibility (https://docs.python.org/2/library/curses.html#curses.curs_set)
    win.keypad(1)               # enable processing of functional keys by curses (ex. arrow keys)              # set a border for the window
    win.nodelay(1)
    show_map(load_map(),win)
    enable_moving(win,load_map())

def enable_moving(win,maze_components):
    global coord_x
    global coord_y
    init_coord()
    while True:
        if coord_x==69 and coord_y==13:
            break
        event = win.getch()
        if event == ord ("q"):
            break
        elif event == curses.KEY_RIGHT :
            if maze_components[coord_y-1][coord_x+1]=='X':
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y,coord_x+1, 'O')
                coord_x=coord_x+1
                win.refresh()
        elif event == curses.KEY_LEFT :
            if maze_components[coord_y-1][coord_x-1]=='X':
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y,coord_x-1, 'O')
                coord_x=coord_x-1
                win.refresh()
        elif event == curses.KEY_DOWN :
            if maze_components[coord_y][coord_x]=='X':
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y+1,coord_x, 'O')
                coord_y=coord_y+1
                win.refresh()
        elif event == curses.KEY_UP :
            if maze_components[coord_y-2][coord_x]=='X':
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y-1,coord_x, 'O')
                coord_y=coord_y-1
                win.refresh()

    curses.endwin()

def main():
    win= curses.initscr()
    open_window(win, load_map())

if __name__ == "__main__":
    main()
