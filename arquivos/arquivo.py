#import pickle

#arquivo = open("xamps.f", "rb")
#aluno = {'Nome':'Eduardo', 'Idade':29}
#pickle.dump(aluno, arquivo)
#arquivo.close

#aluno = pickle.load(arquivo)
#print(aluno)

def teste_lista(l):
    l[0] = True

def teste_mapa(v):
    v['Nome'] = 'Maria'

lista = [False, False, False]
teste_lista(lista)

aluno = {'Nome':'Eduardo'}
teste_mapa(aluno)

a = 2,3

print(teste_lista(a))
