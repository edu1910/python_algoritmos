mpesos = []

for lin in range(3):
    linha = []
    for col in range(3):
        print('['+str(lin)+']'+'['+str(col)+']')
        linha.append(float(input('Digite o peso: ')))
    mpesos.append(linha)

for lin in range(3):
    linhaFmt = ''
    for col in range(3):
        linhaFmt = linhaFmt + format(mpesos[lin][col], '8.2f')
    print(linhaFmt)

