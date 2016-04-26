while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    if nota1 > nota2:
        nota3 = nota1 + nota3
    else:
        nota3 = nota2 + nota3

    media = nota3 / 2

    print("Média:", media)

    if media >= 7:
        print("Aprovado")
    elif media >= 4:
        print("Final")
    else:
        print("Reprovado")

    continuar = input("Deseja continuar (S/N): ")
    if continuar == "N":
        break