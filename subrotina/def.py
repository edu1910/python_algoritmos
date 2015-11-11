def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multiplicacao(num1, num2):
    return num1*num2

#divisao
#num1: dividendo
#num2: divisor
#retorno: quociente (float)
def divisao(num1, num2):
    return num1/num2

#menu
#Desenha o menu principal e retorna a opção selecionada pelo usuário
#retorno: opção selecionada (int)
def menu():
    print('1- Soma')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Potenciação')
    print('0- Sair')

    while True:
        opcao = int(input('Opção: '))
        if opcao >= 0 and opcao <= 5:
            return opcao
        print('Opção inválida!')

def ler_dois_numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    return num1,num2

def opcao_somar():
    n1,n2 = ler_dois_numeros()
    print('Soma='+str(soma(n1,n2)))

def opcao_subtrair():
    n1,n2 = ler_dois_numeros()
    print('Subtração='+str(subtracao(n1,n2)))

def opcao_multiplicar():
    n1,n2 = ler_dois_numeros()
    print('Multiplicação='+str(multiplicacao(n1,n2)))

def opcao_dividir():
    n1,n2 = ler_dois_numeros()
    print('Divisão='+str(divisao(n1,n2)))

def opcao_potenciacao():
    n1,n2 = ler_dois_numeros()
    print('Potenciação='+str(n1**n2))

#Início da aplicação
while True:
    opcao = menu()

    if opcao == 1:
        opcao_somar()
    elif opcao == 2:
        opcao_subtrair()
    elif opcao == 3:
        opcao_multiplicar()
    elif opcao == 4:
        opcao_dividir()
    elif opcao == 5:
        opcao_potenciacao()
    elif opcao == 0:
        break
    
print('Vlw, flw!')
