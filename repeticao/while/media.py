while True:
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))

    if nota1 > nota2:
        media = (nota1 + nota3) / 2
    else:
        media = (nota2 + nota3) / 2

    print('Media = %.2f' % media)

    opcao = ''
    while (opcao != 'S' and opcao != 'N'):
        opcao = input('Deseja calcular a média de outro aluno (S/N): ')

    if opcao == 'N':
        break
