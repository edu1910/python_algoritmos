tentativas = 3
while True:
    senha = input('Senha BOLADA DO SUCESSO: ')
    if senha == 'xamps':
        print('Acertou, mizeravi!')
        break

    print('Você não sabe a senha e eu não digo :D')
    tentativas = tentativas - 1
    if tentativas == 0:
        print('Errou demais, danado!')
        break
