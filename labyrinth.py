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

#this function prints the map to the screen
def show_map(maze_components,win):
    global coord_x
    global coord_y
    for coord_y in range(0,20):
        for coord_x in range(0,70):
                win.addch(coord_y,coord_x,maze_components[coord_y-1][coord_x])
    win.refresh()

#this function loads the map from a txt file to a 2D list
def load_map():
    maze_components=[]
    file = open("map.txt", "r")
    for row in file:
        for i in file:
            maze_components.append(i)
    file.close()
    return maze_components

#this function creates the window for the game
def create_window(win):
    win = curses.newwin(40, 100, 0, 0)
    curses.noecho()
    curses.curs_set(0)
    win.keypad(1)
    win.nodelay(1)
    return win

'''this function handles the when the user wants to move left, and also the score
system'''
def moving_left(win,maze_components):
    global score
    global coord_x
    global coord_y
    if maze_components[coord_y-1][coord_x-1]=='X':
        score=score+10
        pass
    else:
        score=score+1
        win.addch(coord_y,coord_x, ' ')
        win.addch(coord_y,coord_x-1, 'O')
        coord_x=coord_x-1
        win.refresh()

'''this function handles the when the user wants to move right, and also the score
system'''
def moving_right(win,maze_components):
    global score
    global coord_x
    global coord_y
    if maze_components[coord_y-1][coord_x+1]=='X':
        score=score+10
        pass
    else:
        score=score+1
        win.addch(coord_y,coord_x, ' ')
        win.addch(coord_y,coord_x+1, 'O')
        coord_x=coord_x+1
        win.refresh()

'''this function handles the when the user wants to move up, and also the score
system'''
def moving_up(win,maze_components):
    global score
    global coord_x
    global coord_y
    if maze_components[coord_y-2][coord_x]=='X':
        score=score+10
        pass
    else:
        score=score+1
        win.addch(coord_y,coord_x, ' ')
        win.addch(coord_y-1,coord_x, 'O')
        coord_y=coord_y-1
        win.refresh()

'''this function handles the when the user wants to move down, and also the score
system'''
def moving_down(win,maze_components):
    global score
    global coord_x
    global coord_y
    if maze_components[coord_y][coord_x]=='X':
        score=score+10
        pass
    else:
        score=score+1
        win.addch(coord_y,coord_x, ' ')
        win.addch(coord_y+1,coord_x, 'O')
        coord_y=coord_y+1
        win.refresh()

"""the main function calls the other functions in the right sequence and this
function contains also the logic for moving"""
def main():
    lab_components = load_map()
    win = curses.initscr()
    win = create_window(win)
    show_map(lab_components,win)
    init_coord()
    while True:
        win.addch(coord_y,coord_x, 'O')
        win.addstr(22,2, 'Score : ' + str(score) + ' ')
        if coord_x == 69 and coord_y == 13:
            break
        event = win.getch()
        if event == ord ("q"):
            break
        elif event == curses.KEY_LEFT :
            moving_left(win,lab_components)
        elif event == curses.KEY_RIGHT :
            moving_right(win,lab_components)
        elif event == curses.KEY_UP :
            moving_up(win,lab_components)
        elif event == curses.KEY_DOWN :
            moving_down(win,lab_components)
    win = curses.initscr()
    win.clear()
    print("you score: "+str(score))
    time.sleep(3)
    curses.endwin()

if __name__ == "__main__":
    main()
