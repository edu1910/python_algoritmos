from utils import *

palavra_original = input('Digite uma palavra: ')
palavra_escondida = esconder_palavra(palavra_original)
letras_usadas = ""
tentativas = 3

while tentativas > 0:
    print('Palavra: ' + palavra_escondida)
    print('Letras utilizadas: ' + letras_usadas)
    print('Tentativas: ' + str(tentativas))
    letra = input('Digite uma letra ou 0 para sair: ')
    if len(letra) == 1 and letra >= 'a' and letra <= 'z':
        if letras_usadas.find(letra) == -1:
            if len(letras_usadas) > 0:
                letras_usadas += ','
            letras_usadas += letra

            nova_palavra_escondida = troca_sublinha(palavra_original, palavra_escondida, letra)
            if nova_palavra_escondida != palavra_escondida:
                palavra_escondida = nova_palavra_escondida
                print('Acertou!')

                if jogador_ganhou(palavra_escondida):
                    print('Parabéns, você ganhou!')
            else:
                print('Errou mizeravelmente!')
                tentativas -= 1
        else:
            print('Letra já utilizada!')
    elif letra == '0':
        break
    else:
        print('Eim?!')

if tentativas == 0:
    print('Você perdeu! A palavra era ' + palavra_original)