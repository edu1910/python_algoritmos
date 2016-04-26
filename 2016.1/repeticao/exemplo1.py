qtd_idades = 2
idades = []

for numero in range(qtd_idades):
    idade = int(input('Digite a idade ' + str(numero+1) + ': '))
    idades.append(idade)

idades.sort()

for numero in range(qtd_idades):
    print('Idade ' + str(numero+1) + ': ' + str(idades[numero]))
