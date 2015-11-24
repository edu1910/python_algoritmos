alunos = []
continuar = True

while continuar:
    aluno = {}
    aluno['nome'] = input('Nome: ')
    aluno['idade'] = input('Idade: ')
    alunos.append(aluno)
    continuar = input('Continuar (SIM)? ') == 'SIM'

arquivo = open('alunos.txt', 'a')

for aluno in alunos:
    chaves = list(aluno.keys())
    chaves.sort(reverse=True)
    for chave in chaves:
        arquivo.write(chave + ': ' + aluno[chave] + '\n')

arquivo.close()
