sair = False

while (not sair):
    print('-----------')
    print('CALCULADORA')
    print('-----------')
    print('1- Soma')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('X- Sair')
    print('---')

    while True:
        opcao = input('Opção: ')

        if (opcao == '1') or (opcao == '2') or (opcao == '3') or (opcao == '4') or (opcao == 'X'):
            break

        print('Opção inválida!')

    if opcao == 'X':
        sair = True

    if opcao == '1':
        print('SOMA!')
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
        soma = num1 + num2

        print('Soma=%.2f' % soma)
        input('Pressione enter para continuar... ')
