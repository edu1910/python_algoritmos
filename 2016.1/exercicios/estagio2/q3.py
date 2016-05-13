nomes = []
continuar = True

while continuar:
    nome = input("Digite um nome: ")
    nomes.append(nome.strip())
    continuar = (input("Deseja continuar? (S/N) ") != 'N')

nomes_ordenados = []

while len(nomes) > 0:
    menor_idx = 0
    for idx in range(1, len(nomes)):
        if (nomes[idx] < nomes[menor_idx]):
            print("Descobri um índice menor:",idx)
            menor_idx = idx
    nomes_ordenados.append(nomes.pop(menor_idx))

nomes = nomes_ordenados

for idx in range(len(nomes)):
    print(str(idx+1),'-',nomes[idx])
