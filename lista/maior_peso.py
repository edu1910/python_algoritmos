matriz = []

for lin in range(3):
    pesos = []
    for col in range(3):
       peso = float(input('Peso ['
                          +str(lin+1)+','+str(col+1)+']: '))
       pesos.append(peso)
    matriz.append(pesos)

maior = 0

for linha in matriz:
    for peso in linha:
        if peso > maior:
            maior = peso

print(maior)



