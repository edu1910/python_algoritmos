'''
Código que não deixa repetir as palavras
'''

import random

palavras = ['casa','bola','pena','cafe','gato','xbox','azul']
sorteadas = []

while len(sorteadas) < len(palavras):
    indice = random.randint(0, len(palavras)-1) 
    if not(indice in sorteadas):
        sorteadas.append(indice)
        print('Sorteada: ' + palavras[indice])

print('Acabaram as palavras!')