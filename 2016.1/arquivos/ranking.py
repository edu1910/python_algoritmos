import pickle

def inserir_ranking(ranking, nome, pontuacao):
    recorde = {'nome':nome, 'pontuacao':pontuacao}

    posicao = len(ranking)

    for idx in range(len(ranking)):
        if ranking[idx]['pontuacao'] < pontuacao:
            posicao = idx
            break

    ranking.insert(posicao, recorde)

def imprimir_ranking(ranking):
    for recorde in ranking:
        print(recorde['nome'] + ': ' + str(recorde['pontuacao']))

def salvar(ranking):
    arquivo = open('ranking', 'wb')
    pickle.dump(ranking, arquivo)
    arquivo.close()

def carregar():
    try:
        arquivo = open('ranking', 'rb')
        ranking = pickle.load(arquivo)
        arquivo.close()
    except:
        ranking = []

    return ranking

ranking = carregar()
print('\n\nRANKING ATUAL:\n')
imprimir_ranking(ranking)
print('\n\n')

nome = input('Nome: ')
pontuacao = int(input('Pontuação: '))

inserir_ranking(ranking, nome, pontuacao)
print('\n\nRANKING ATUALIZADO:\n')
imprimir_ranking(ranking)
salvar(ranking)
