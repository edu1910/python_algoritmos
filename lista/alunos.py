qtd = int(input('Quantidade de alunos: '))
qtd_notas = 3

alunos = []

#Captura do nome e notas do danado do aluno
for idx in range(qtd):
    aluno = []

    print('--- ALUNO ' + str(idx+1) + ' ---')
    nome = input('Digite o nome do aluno: ')
    aluno.append(nome)

    for inota in range(qtd_notas):
        nota = float(input('Digite a nota ' + str(inota+1) + ': '))
        aluno.append(nota)

    nota = 0
    for inota in range(qtd_notas):
        nota = nota + aluno[inota+1]

    aluno.append(nota/3)
    alunos.append(aluno)

#Imprimir informações do aluno na tela
for idx in range(qtd):
    aluno = alunos[idx]

    print('Nome: ' + aluno[0])
    
    for inota in range(qtd_notas):
        print('Nota ' + str(inota+1) + ': ' + str(aluno[inota+1]))

    print('Média: ' + str(aluno[qtd_notas+1]))
              
