total = 0

while True:
    valor = input("Digite um número (SAIR para sair): ")
    if valor == 'SAIR':
        break
    try:
        total = total + float(valor)
    except:
        pass
    print("Total =", total)
