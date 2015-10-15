continuar = True
idades = []

while continuar:
    idade = int(input('Digite uma idade: '))
    idades.append(idade)

    opcao = input('Deseja digitar outra idade (S/N): ')
    continuar = (opcao == 'S')

maior = 0

for idade in idades:
    if idade > maior:
        maior = idade

print('Maior: '+str(maior))
