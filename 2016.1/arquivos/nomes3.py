import pickle

def escreve_arquivo(lista_pessoas):
    arquivo = open("pessoas_b", "wb")

    pickle.dump(lista_pessoas, arquivo)

    arquivo.close()

def le_arquivo():
    try:
        arquivo = open("pessoas_b", "rb")

        lista = pickle.load(arquivo)

        arquivo.close()
    except:
        lista = []

    return lista

pessoas = le_arquivo()

print("LOG: pessoas = " + str(pessoas))

for idx in range(1):
    pessoa = {}
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa)

print("LOG: pessoas = " + str(pessoas))

escreve_arquivo(pessoas)