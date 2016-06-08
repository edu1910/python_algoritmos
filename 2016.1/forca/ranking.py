import pickle

QTD_RECORDES = 10
ARQUIVO_RECORDE = "recorde.rec"

__NOME = 'nome'
__PONTUACAO = 'pontuacao'

def obter_nome(recorde):
    return recorde[__NOME]

def obter_pontuacao(recorde):
    return recorde[__PONTUACAO]

def inserir_recorde(nome, pontuacao):
    ranking = __carregar_ranking()

    posicao = __posicao_recorde(ranking, pontuacao)
    if posicao < QTD_RECORDES:
        recorde = {__NOME:nome, __PONTUACAO:pontuacao}

        ranking.insert(posicao, recorde)
        ranking = ranking[:QTD_RECORDES]
        __salvar_ranking(ranking)

def verificar_recorde(pontuacao):
    pos_recorde = 0

    if pontuacao > 0:
        ranking = __carregar_ranking()

        posicao = __posicao_recorde(ranking, pontuacao)
        if posicao < QTD_RECORDES:
            pos_recorde = posicao + 1

    return pos_recorde

def obter_ranking():
    return __carregar_ranking()

def __posicao_recorde(ranking, pontuacao):
    posicao = len(ranking)

    for idx in range(len(ranking)):
        reg = ranking[idx]
        if reg[__PONTUACAO] < pontuacao:
            posicao = idx
            break

    return posicao

def __carregar_ranking():
    ranking = []

    try:
        arq = open(ARQUIVO_RECORDE, "rb")
        ranking = pickle.load(arq)
        arq.close()
    except:
        pass

    return ranking

def __salvar_ranking(ranking):
    try:
        arq = open(ARQUIVO_RECORDE, "wb")
        pickle.dump(ranking, arq)
        arq.close()
    except:
        pass