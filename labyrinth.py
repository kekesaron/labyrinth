import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

coord_x=1
coord_y=1
score=0

def init_coord():
    global coord_x
    coord_x=1
    global coord_y
    coord_y=1

def show_map(maze_components,win):
    global coord_x
    global coord_y
    for coord_y in range(0,20):
        for coord_x in range(0,70):
                win.addch(coord_y,coord_x,maze_components[coord_y-1][coord_x])
    win.refresh()

def load_map():
    maze_components=[]
    file = open("map.txt", "r")
    for row in file:
        for i in file:
            maze_components.append(i)
    file.close()
    return maze_components

def create_window(win):
    win = curses.newwin(40, 100, 0, 0)  # Init window object
    curses.noecho()             # Disable default printing of inputs
    curses.curs_set(0)          # Hiding cursor visibility
    win.keypad(1)               # enable processing of functional keys by curses (ex. arrow keys)
    win.nodelay(1)
    return win

def moving(win,maze_components):
    global score
    global coord_x
    global coord_y
    init_coord()
    while True:
        win.addch(coord_y,coord_x, 'O')
        win.addstr(22,2, 'Score : ' + str(score) + ' ')
        if coord_x==69 and coord_y==13:
            break
        event = win.getch()
        if event == ord ("q"):
            break
        elif event == curses.KEY_RIGHT :
            score=score+1
            if maze_components[coord_y-1][coord_x+1]=='X':
                score=score+9
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y,coord_x+1, 'O')
                coord_x=coord_x+1
                win.refresh()
        elif event == curses.KEY_LEFT :
            score=score+1
            if maze_components[coord_y-1][coord_x-1]=='X':
                score=score+9
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y,coord_x-1, 'O')
                coord_x=coord_x-1
                win.refresh()
        elif event == curses.KEY_DOWN :
            score=score+1
            if maze_components[coord_y][coord_x]=='X':
                score=score+9
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y+1,coord_x, 'O')
                coord_y=coord_y+1
                win.refresh()
        elif event == curses.KEY_UP :
            score=score+1
            if maze_components[coord_y-2][coord_x]=='X':
                score=score+9
                pass
            else:
                win.addch(coord_y,coord_x, ' ')
                win.addch(coord_y-1,coord_x, 'O')
                coord_y=coord_y-1
                win.refresh()
    win=curses.initscr()
    win.clear()
    print("you score: "+str(score))
    time.sleep(3)
    curses.endwin()

def main():
    maze_components=load_map()
    win = curses.initscr()
    win = create_window(win)
    show_map(maze_components,win)
    moving(win,maze_components)

if __name__ == "__main__":
    main()
