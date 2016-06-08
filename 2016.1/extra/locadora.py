import pickle
import os

'''
Limpa a tela Windows/Linux
'''
def clear():
    os.system("cls")
    os.system("clear")

'''
Captura um número inteiro tratando a exceção
'''
def input_int(prompt):
    valor = 0

    while True:
        try:
            valor = int(input(prompt))
            break
        except:
            print('Valor inválido!')

    return valor

'''
Captura um número real tratando a exceção
'''
def input_float(prompt):
    valor = 0

    while True:
        try:
            valor = float(input(prompt))
            break
        except:
            print('Valor inválido!')

    return valor

'''
Exibe o menu principal e retorna a opção selecionada
'''
def opcao_menu():
    opcao = ''
    opcoes_validas = ['1','2','3']

    print("--------------------")
    print("LOCADORA DE VEÍCULOS")
    print("--------------------")
    print("1 - Retirada")
    print("2 - Devolução")
    print("3 - Sair")
    while True:
        opcao = input("Opção: ")
        if opcao in opcoes_validas:
            break
        print("Opção inválida!")

    return opcao

'''
Captura as informações e cria uma retirada 
'''
def fazer_retirada():
    retirada = {'NOME':'', 'CNH':'', 'VL_DIARIA':0.0, 'VL_KM_EXTRA':0.0, 
                'LIMITE_KM':0, 'KM_RETIRADA':0, 'DATA_RETIRADA':''}

    print('-------------------')
    print('RETIRADA DE VEÍCULO')
    print('-------------------')
    retirada['NOME'] = input('Nome do cliente: ')
    retirada['CNH'] = input('Número da CNH: ')
    retirada['VL_DIARIA'] = input_float('Valor da diária: ')
    retirada['VL_KM_EXTRA'] = input_float('Valor do km extra: ')
    retirada['LIMITE_KM'] = input_int('Limite de km (0 para sem limite): ')
    retirada['KM_RETIRADA'] = input_int('KM na retirada: ')
    retirada['DATA_RETIRADA'] = input('Data da retirada: ')

    confirmacao = input('\nConfirma cadastro da retirada (S/N)? ')
    if confirmacao == 'S':
        print('Retirada cadastrada!')
    else:
        retirada = None

    print()

    return retirada

'''
Lista as retiradas e captura as informações e faz uma devolução
'''
def fazer_devolucao(retiradas):
    devolucao_ok = False

    print('--------------------')
    print('DEVOLUÇÃO DE VEÍCULO')
    print('--------------------')

    for idx in range(len(retiradas)):
        print(str(idx+1) + ' - ' + retiradas[idx]['NOME'])

    while True:
        num_retirada = input_int('\nQual a retirada deseja finalizar (0 para voltar)? ')
        if num_retirada >= 0 and num_retirada <= len(retiradas):
            break
        print('Retirada inexistente!')

    print()
    if num_retirada > 0:
        retirada = retiradas[num_retirada-1]
        print('Cliente: ' + retirada['NOME'])
        print('Data da retirada: ' + retirada['DATA_RETIRADA'])
        print('--')

        diaras = input_int('Número de diárias utilizadas: ')
        km_atual = input_int('KM atual: ')
        adicional = input_float('Valor adicional: ')

        print('--')

        total = diaras * retirada['VL_DIARIA'] + adicional
        if retirada['VL_KM_EXTRA'] != 0:
            total_rodado = km_atual - retirada['KM_RETIRADA']
            extra = total_rodado - retirada['LIMITE_KM']
            if extra > 0:
                total = total + (extra * retirada['VL_KM_EXTRA'])

        print('Total: R$%.2f' % total)
        confirmacao = input('\nConfirma a devolução (S/N)? ')
        if confirmacao == 'S':
            retiradas.pop(num_retirada-1)
            print('Devolução concluída!')
            devolucao_ok = True

        print()

    return devolucao_ok

'''
Salva lista de retiradas no arquivo
'''
def salvar_retiradas(retiradas):
    arquivo = open("retiradas.loc", "wb")
    pickle.dump(retiradas, arquivo)
    arquivo.close()

'''
Carrega lista de retiradas do arquivo ou cria uma lista vazia
'''
def carregar_retiradas():
    try:
        arquivo = open("retiradas.loc", "rb")
        retiradas = pickle.load(arquivo)
        arquivo.close()
    except:
        retiradas = []

    return retiradas

'''
Programa principal
'''
retiradas = carregar_retiradas()

while True:
    clear()
    opcao = opcao_menu()
    if opcao == '3':
        break
    elif opcao == '1':
        clear()
        retirada = fazer_retirada()

        if retirada != None:
            retiradas.append(retirada)
            salvar_retiradas(retiradas)
    elif opcao == '2':
        clear()
        if fazer_devolucao(retiradas):
            salvar_retiradas(retiradas)
