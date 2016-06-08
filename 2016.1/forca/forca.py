'''
Teste da biblioteca ranking
'''

import ranking

def fill(word, size):
    strlen = len(word)
    newstr = word

    for idx in range(size - strlen):
        newstr += " "

    return newstr


pontuacao = int(input('Digite a pontuação: '))

num_recorde = ranking.verificar_recorde(pontuacao)
if num_recorde > 0:
    print("Parabéns! Você quebrou o recorde de número " + str(num_recorde) + "!")
    nome = input('Digite seu nome: ')

    ranking.inserir_recorde(nome, pontuacao)
else:
    print("Que pena! Você não quebrou o recorde.")

print("\n")
print("--------------------")
print("RANKING DE PONTUAÇÃO")
print("--------------------")
recordes = ranking.obter_ranking()

if len(recordes) > 0:

    for idx in range(len(recordes)):
        recorde = recordes[idx]
        nome = ranking.obter_nome(recorde)
        pont = str(ranking.obter_pontuacao(recorde))

        print("#%02d " % (idx+1), end="")
        print(fill(nome, 30), end="")
        print("%8s" % pont)
else:
    print('Nenhum recorde registrado.')

print("\n")







