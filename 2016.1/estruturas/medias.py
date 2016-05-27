qtd_alunos = 1
qtd_notas  = 3

alunos = []

def calc_media(notas):
    media = 0
    for nota in notas:
        media += nota
    return media/len(notas)

for aluno in range(qtd_alunos):
    print('-----------------------')
    print('ALUNO Nº'+str(aluno+1))
    print('-----------------------')

    nome = input('Nome: ')
    notas = []

    for nota in range(qtd_notas):
        notas.append(float(input('Nota '+str(nota+1)+': ')))

    aluno = {'nome': nome, 'notas': notas}
    alunos.append(aluno)

for aluno in range(qtd_alunos):
    print('-----------------------')
    print('ALUNO: ' + alunos[aluno]['nome'])

    media = calc_media(alunos[aluno]['notas'])

    print('MÉDIA: ' + '%.1f' % media)
    print('-----------------------')
