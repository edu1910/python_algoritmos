import curses

def desenha_cursor(janela, posicao_antiga, posicao):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    y = int((posicao-1) / 20)
    x = int((posicao-1) % 20)
    janela.addstr(y, x, ' ', curses.color_pair(1))

    if posicao_antiga > 0:
        y_antiga = int((posicao_antiga-1) / 20)
        x_antiga = int((posicao_antiga-1) % 20)
        janela.addstr(y_antiga, x_antiga, ' ')
    janela.refresh()

tela = curses.initscr()
curses.noecho()
curses.start_color()
curses.curs_set(False)
tela.clear()

posicao = 1

win = curses.newwin(21,21,0,0)
desenha_cursor(win, 0, posicao)

ch = win.getch()
while ch != '\n':
    posicao_bkp = posicao

    ch = chr(ch)
    if ch == 'a':
        posicao -= 1
    elif ch == 'd':
        posicao += 1
    elif ch == 's':
        posicao += 20
    elif ch == 'w':
        posicao -= 20

    if posicao < 1 or posicao > 400:
        posicao = posicao_bkp

    if posicao != posicao_bkp:
        desenha_cursor(win, posicao_bkp, posicao)

    ch = win.getch()

curses.echo()
curses.endwin()