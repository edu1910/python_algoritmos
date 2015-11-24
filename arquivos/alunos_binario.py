import pickle

continuar = True

try:
    arquivo = open('alunos.bin', 'rb')
    alunos = pickle.load(arquivo)
    arquivo.close()
except:
    alunos = []    

print('Carregado:')
print(alunos)

while continuar:
    aluno = {}
    aluno['nome'] = input('Nome: ')
    aluno['idade'] = input('Idade: ')
    alunos.append(aluno)
    continuar = input('Continuar (SIM)? ') == 'SIM'

arquivo = open('alunos.bin', 'wb')
pickle.dump(alunos, arquivo)
arquivo.close()
