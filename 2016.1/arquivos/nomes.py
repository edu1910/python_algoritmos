def escreve_arquivo(lista_nomes):
    arquivo = open("nomes", "w")

    for nome in lista_nomes:
        arquivo.write(nome + "\n")

    arquivo.close()

def le_arquivo():
    try:
        arquivo = open("nomes", "r")

        lista = []
        linha = arquivo.readline()

        while linha != '':
            lista.append(linha[:-1])
            linha = arquivo.readline()

        arquivo.close()
    except:
        lista = []

    return lista

nomes = le_arquivo()

print("LOG: nomes = " + str(nomes))

for idx in range(3):
    nomes.append(input('Digite um nome: '))

print("LOG: nomes = " + str(nomes))

escreve_arquivo(nomes)