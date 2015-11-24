arq = open("cliente.xamps", "w")

for numCliente in range(5):
    nome = input('Nome: ')
    idade = input('Idade: ')
    cpf = input('CPF: ')
    arq.write('---------------------\n')
    arq.write('Nome : ' + nome + '\n')
    arq.write('Idade: ' + idade + '\n')
    arq.write('CPF  : ' + cpf + '\n')

arq.close()
