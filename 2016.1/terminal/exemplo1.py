import curses

screen = curses.initscr()

curses.start_color()
curses.cbreak()
curses.noecho()
curses.curs_set(False)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_YELLOW)

screen.clear()

#screen.addstr(5, 20, "Olá, mundão!", curses.color_pair(2))
#screen.addstr(5, 25, "Olá, mundão!", curses.color_pair(1))
#screen.refresh()

#screen.getkey()
#screen.clear()

win = curses.newwin(20, 20, 5, 5)

ch = 0
while ch != '0':
    ch = win.getkey()
    win.addstr(5, 5, ch)

win.refresh()

win.getkey()

curses.endwin()