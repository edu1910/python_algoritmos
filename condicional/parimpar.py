numero = int(input('Entre com um número inteiro que eu magicamente direi se é par ou ímpar: '))

print('Realizando a mágica...')

if 0 == (numero % 2):
    print('TCHARAN! O número é PAR.')
elif 0 != (numero % 2):
    print('TCHARAN! O número é ÍMPAR.')
else:
    print('TCHARAN!')
