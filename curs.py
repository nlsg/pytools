#!/usr/bin/python
import sys,os,getopt,curses

def init_curs():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)

    render_screen(stdscr)
    play_w = {}

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def render_screen(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()

    input_w = {}
    play_w = {}
    play_score = 0
    play_points = {}
    max_points = 301
    player_amount = 2
    once = True
    resize = True
    title = "Dart Counter v1.0"
    height_, width_ = stdscr.getmaxyx()
    for i in range(player_amount):
        play_points[i] = 0

    start_w = curses.newwin(height_//2,width_//2,height_//4,width_//4)
    set = {}
    set[0] = "amount of players: "
    set[1] = "mode: "
    curses.curs_set(1)
    curses.echo()
    it = 1
    while (True):
        try:
            start_w.box(0,0)
            start_w.addstr(1,1,set[0])
            start_w.addstr(2,1,set[1])
            start_w.attron(curses.A_STANDOUT)
            start_w.addstr("301")
            start_w.attroff(curses.A_STANDOUT)

            start_w.move(1,len(set[0]))
            player_amount = int(start_w.getstr())
        except:
            start_w.clear()
            start_w.refresh()
            continue
        curses.curs_set(0)
        curses.noecho()
        break

    it = player_amount - 1
    while (k != ord('q')):
        it += 1
        # Initialization
        height, width = stdscr.getmaxyx()
        if ((width != width_) or (height != height_)):
            resie = True
            width_ = width
            height_ = height

        stdscr.move(0,0)
        stdscr.attron(curses.A_BOLD)
        stdscr.clrtoeol()
        stdscr.addstr(0,(width//2) - (len(title))//2,title)
        stdscr.attroff(curses.A_BOLD)

        cursor_x = min(width-1, cursor_x)

        cursor_y = min(height-1, cursor_y)

        statusbarstr = "Ctrl + C to exit | Pos: {}, {} | it: {}[{}]".format(cursor_x, cursor_y, it, (it % player_amount) + 1)

        start_y = int((height // 2) - 2)

        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.refresh()

        #init player_windows
        while (once):
            for i in range(player_amount):
                play_w[i] = curses.newwin(height-2,width//player_amount,1,width//player_amount*i)
            once = False
        while (resize):
            for i in range(player_amount):
                play_w[i].box(0,0)
                play_w[i].attron(curses.A_BOLD)
                play_w[i].addstr(0,1,"player{}".format(i+1))
                play_w[i].attroff(curses.A_BOLD)
                play_w[i].addstr(1,2,"  0 - {}".format(max_points))
                play_w[i].refresh()
            resize = False

        input_w = curses.newwin(3,width//(player_amount*2),height-6,width//player_amount*(it % player_amount)+(width//(player_amount*4)))
        
        curses.curs_set(1)
        curses.echo()

        #get score
        while True:
            try:
                input_w.box(0,0)
                input_w.addstr(0,(width//(player_amount*2))//2 - len("player{")//2,"player{}".format((it % player_amount)+ 1))
                input_w.addstr(1,1,"score: ")
                input_w.move(1,8)
                input = input_w.getstr()
                play_score = int(eval(input))
            except:
                input_w.clear()
                input_w.refresh()
                continue
            break
        input_w.clear()
        input_w.refresh()
        
        play_points[it % player_amount] += play_score
        if (play_points[it % player_amount] > max_points):
            play_points[it % player_amount] -= play_score
        elif (play_points[it % player_amount] == max_points):
            end_w = curses.newwin(height//2,width//2,height//4,width//4)
            end_w.box(0,0)
            h_,w_ = end_w.getmaxyx()

            win_str = {}
            win_str[0] = "player{} winns!".format(it % player_amount)
            win_str[1] = "in {} rounds".format(it//player_amount)
            end_w.addstr(1,(w_//2) - (len(win_str[0])//2),win_str[0])
            end_w.addstr(2,(w_//2) - (len(win_str[1])//2),win_str[1])
            end_w.refresh()
            end_w.getch()
            break #return from main-while

        play_w[it % player_amount].addstr("\t + ({})".format(input))
        play_w[it % player_amount].addstr((it//player_amount)+1 ,1,"{} - {}".format(play_points[it % player_amount],max_points - play_points[it % player_amount]))
        play_w[it % player_amount].refresh()
        
        stdscr.refresh()
        curses.noecho()
        curses.curs_set(0)
        input_w.refresh()
        # Wait for next input
        #k = stdscr.getch()

if __name__ == "__main__":
    init_curs()
