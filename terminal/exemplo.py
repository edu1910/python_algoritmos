import curses

tela = curses.initscr()
curses.start_color()
curses.curs_set(False)
tela.clear()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)

janela1 = curses.newwin(20, 20, 0, 0)
janela2 = curses.newwin(10, 10, 20, 20)

janela1.addstr(0, 0, 'Carlos Eduardo Carneiro', curses.color_pair(1))
janela1.refresh()
janela2.addstr(0, 0, 'XXXXXX', curses.color_pair(2)) 
janela2.refresh()
janela2.getch()

curses.endwin()