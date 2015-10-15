linhas = 3
colunas = 3
jogador = 'X'
tabuleiro = []
ganhador = 'VELHA'
tem_ganhador = False

#Início do tabuleiro
for l in range(linhas):
    linha = []
    for c in range(colunas):
        linha.append(' ')
    tabuleiro.append(linha)

while True:    
    #Imprimindo o tabuleiro
    colunas_formatada = '   '
    for c in range(colunas):
        colunas_formatada += chr(ord('a') + c) + ' '
    print(colunas_formatada)
    
    for l in range(linhas):
        linha = tabuleiro[l]
        linha_formatada = str(l+1) + ' |'
        for coluna in linha:
            linha_formatada += coluna + '|'
        print(linha_formatada)

    #Se já tem ganhador, termina o jogo
    if tem_ganhador:
        break

    linha = ''

    print('Vez do jogador ' + jogador)

    #Obtndo linha e coluna válidas
    while True:
        while True:
            linha = input('Linha (1-'+str(linhas)+'): ')
            if (len(linha) == 1) and (ord(linha) >= ord('1')) and (ord(linha) <= ord(str(linhas))):
                break

        coluna = ''

        while True:
            coluna = input('Coluna (a-'+chr(ord('a')+colunas-1)+'): ')
            if (len(coluna) == 1) and(ord(coluna) >= ord('a')) and (ord(coluna) <= (ord('a')+colunas-1)):
                break

        linha = int(linha) - 1
        coluna = ord(coluna) - ord('a')

        if tabuleiro[linha][coluna] == ' ':
            break

        print('Jogada não permitida')

    tabuleiro[linha][coluna] = jogador

    #Verificando se jogador ganhou na linha
    for linha in tabuleiro:
        if not (' ' in linha):
            if ('X' in linha) and (not ('O' in linha)):
                tem_ganhador = True
                ganhador = 'X'
                break

            if ('O' in linha) and (not ('X' in linha)):
                tem_ganhador = True
                ganhador = 'O'
                break

    #Verificando se jogador ganhou na diagonal
    if not tem_ganhador:
        lcolunas = []

        c = 0
        for linha in tabuleiro:
            lcolunas.append(linha[c])
            c = c + 1

        if not (' ' in lcolunas):
            if ('X' in lcolunas) and (not ('O' in lcolunas)):
                tem_ganhador = True
                ganhador = 'X'

            if ('O' in lcolunas) and (not ('X' in lcolunas)):
                tem_ganhador = True
                ganhador = 'O'

    #Verificando se jogador ganhou na outra diagonal
    if not tem_ganhador:
        lcolunas = []

        c = colunas - 1
        for linha in tabuleiro:
            lcolunas.append(linha[c])
            c = c - 1

        if not (' ' in lcolunas):
            if ('X' in lcolunas) and (not ('O' in lcolunas)):
                tem_ganhador = True
                ganhador = 'X'

            if ('O' in lcolunas) and (not ('X' in lcolunas)):
                tem_ganhador = True
                ganhador = 'O'

    #Verificando se jogador ganhou na coluna
    if not tem_ganhador:
        for c in range(colunas):
            lcolunas = []
            for linha in tabuleiro:
                lcolunas.append(linha[c])

            if not (' ' in lcolunas):
                if ('X' in lcolunas) and (not ('O' in lcolunas)):
                    tem_ganhador = True
                    ganhador = 'X'
                    break

                if ('O' in lcolunas) and (not ('X' in lcolunas)):
                    tem_ganhador = True
                    ganhador = 'O'
                    break

    #Verificando se deu velha
    if not tem_ganhador:  
        tem_ganhador = True
        for linha in tabuleiro:
            if ' ' in linha: #Se tiver espaço em branco na linha, o jogo não acabou
                tem_ganhador = False
                break

    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

print('Ganhador: ' + ganhador)
