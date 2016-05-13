def situacao_aluno(nota1, nota2, nota3):
    situacao = ''
    media = calcula_media(nota1, nota2, nota3)

    if media >= 7:
        situacao = 'A'
    elif media >= 4:
        situacao = 'F'
    else:
        situacao = 'R'

    return situacao

def calcula_media(nota1, nota2, nota3):
    return (nota3 + (nota1 if nota1 > nota2 else nota2))/2

def input_float(prompt):
    return float(input(prompt))

def imprime_situacao_media(situacao, media):
    situacao_str = ''
    if situacao == 'A':
        situacao_str = 'Aprovado'
    elif situacao == 'F':
        situacao_str = 'Final'
    else:
        situacao_str = 'Reprovado'

    print(situacao_str, 'média = '+str(media), sep=', ')

'''
PROGRAMA PRINCIPAL
'''
print('Olá, usuário bolado do sucesso!')
print('Vamos lá saber qual é a sua situação...')
avaliacao1 = input_float('Digite a nota da primeira avaliação: ')
avaliacao2 = input_float('Digite a nota da segunda avaliação: ')
avaliacao3 = input_float('Digite a nota da terceira avaliação: ')
media = calcula_media(avaliacao1, avaliacao2, avaliacao3)
situacao = situacao_aluno(avaliacao1, avaliacao2, avaliacao3)
imprime_situacao_media(situacao, media)



