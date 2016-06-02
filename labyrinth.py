import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

coord_x = 1
coord_y = 1
fogx = 3
fogy = 3
score = 0
fogx_start = 0
fogy_start = 0
last_move_x = 0


def init_coord():
    global coord_x
    coord_x = 1
    global coord_y
    coord_y = 1


def show_map(maze_components, win):
    global coord_x
    global coord_y
    for coord_y in range(0, 20):
        for coord_x in range(-1, 70):
            # win.addch(coord_y, coord_x, maze_components[coord_y-1][coord_x])
            win.refresh()


# this function loads the map from a txt file to a 2D list
def load_map():
    maze_components = []
    file = open("map.txt", "r")
    for row in file:
        for i in file:
            maze_components.append(i)
    file.close()
    return maze_components


# this function creates the window for the game
def create_window(win):
    win = curses.newwin(40, 100, 0, 0)
    curses.noecho()
    curses.curs_set(0)
    win.keypad(1)
    win.nodelay(1)
    return win


# this function handles the when  user wants to move left, and also the score
# system
def moving_left(win, maze_components):
    global score
    global coord_x
    global coord_y
    global fogx
    global fogy
    global fogx_start
    global fogy_start
    if maze_components[coord_y-1][coord_x-1] == 'X':
        score = score+10
        pass
    else:
        score = score+1
        win.addch(coord_y, coord_x, ' ')
        win.addch(coord_y, coord_x-1, 'O')
        coord_x = coord_x-1
        fogx = fogx - 1
        fogx_start = fogx_start - 1
        for i in range(fogy_start, fogy):
            for j in range(fogx_start, fogx):
                win.addch(i, j, maze_components[i-1][j])
        win.refresh()


# this function handles the when the user wants to move right, and the score
# system
def moving_right(win, maze_components):
    global score
    global coord_x
    global coord_y
    global fogx
    global fogy
    global fogx_start
    global fogy_start
    if maze_components[coord_y-1][coord_x+1] == 'X':
        score = score+10
        pass
    else:
        score = score+1
        fogx = fogx + 1
        win.addch(coord_y, coord_x, ' ')
        win.addch(coord_y, coord_x+1, 'O')
        coord_x = coord_x+1
        for i in range(fogy_start, fogy):
            for j in range(fogx_start, fogx):
                win.addch(i, j, maze_components[i-1][j])
        fogx_start = fogx_start + 1
        win.refresh()


def moving_up(win, maze_components):
    global score
    global coord_x
    global coord_y
    global fogy
    global fogx
    global fogx_start
    global fogy_start
    if maze_components[coord_y-2][coord_x] == 'X':
        score = score+10
        pass
    else:
        win.addch(coord_y, coord_x, ' ')
        win.addch(coord_y-1, coord_x, 'O')
        score = score - 1
        coord_y = coord_y - 1
        fogy = fogy - 1
        fogy_start = fogy_start - 1
        for i in range(fogy_start, fogy-1):
            for j in range(fogx_start, fogx):
                win.addch(i, j, maze_components[i-1][j])
        win.refresh()


def moving_down(win, maze_components):
    global score
    global coord_x
    global coord_y
    global fogy
    global fogx
    global fogx_start
    global fogy_start
    if maze_components[coord_y][coord_x] == 'X':
        score = score+10
        pass
    else:
        win.addch(coord_y, coord_x, ' ')
        win.addch(coord_y+1, coord_x, 'O')
        fogy = fogy + 1
        coord_y = coord_y+1
        for i in range(fogy_start, fogy):
            for j in range(fogx_start, fogx):
                win.addch(i, j, maze_components[i-1][j])
        fogy_start = fogy_start + 1
        win.refresh()


def main():
    lab_components = load_map()
    win = curses.initscr()
    win = create_window(win)
    show_map(lab_components, win)
    init_coord()
    while True:
        win.addch(coord_y, coord_x, 'O')
        win.addstr(22, 2, 'Score : ' + str(score) + ' ')
        if coord_x == 69 and coord_y == 13:
            break
        event = win.getch()
        if event == ord("q"):
            break
        elif event == curses.KEY_LEFT:
            moving_left(win, lab_components)
        elif event == curses.KEY_RIGHT:
            moving_right(win, lab_components)
        elif event == curses.KEY_UP:
            moving_up(win, lab_components)
        elif event == curses.KEY_DOWN:
            moving_down(win, lab_components)

    win = curses.initscr()
    win.clear()
    print("you score: "+str(score))
    time.sleep(3)
    curses.endwin()

if __name__ == "__main__":
    main()

