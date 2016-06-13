def palavra_valida(string):
    valida = True

    for ch in string:
        if not (ch >= 'a' and ch <= 'z'):
            valida = False
            break

    return valida

def esconder_palavra(palavra_original):
    palavra_escondida = ''
    for idx in range(len(palavra_original)):
        palavra_escondida += '_ '
    return palavra_escondida.strip()

def troca_sublinha(palavra_original, palavra_escondida, letra):
    for idx in range(len(palavra_original)):
        if palavra_original[idx] == letra:
            palavra_escondida = palavra_escondida[:idx*2] + letra + palavra_escondida[idx*2+1:]
    return palavra_escondida

def jogador_ganhou(palavra_escondida):
    return palavra_escondida.find('_') == -1
