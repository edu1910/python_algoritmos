def escreve_arquivo(lista_pessoas):
    arquivo = open("pessoas", "w")

    for pessoa in lista_pessoas:
        arquivo.write(pessoa['nome'] + ',' + str(pessoa['idade']) + "\n")

    arquivo.close()

def le_arquivo():
    try:
        arquivo = open("pessoas", "r")

        lista = []
        linha = arquivo.readline()

        while linha != '':
            linha = linha[:-1].split(sep=',')
            if len(linha) == 2:
                pessoa = {'nome':linha[0], 'idade':int(linha[1])}
                lista.append(pessoa)
            linha = arquivo.readline()

        arquivo.close()
    except:
        lista = []

    return lista

pessoas = le_arquivo()

print("LOG: pessoas = " + str(pessoas))

for idx in range(3):
    pessoa = {}
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa)

print("LOG: pessoas = " + str(pessoas))

escreve_arquivo(pessoas)