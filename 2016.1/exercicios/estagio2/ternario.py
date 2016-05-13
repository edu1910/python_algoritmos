num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))


'''
if num1 > num2:
    print("Número 1 é maior")
else:
    print("Número 1 não é maior")
'''

print("Num1" if num1 > num2 else "Iguais" if num1 == num2 else "Num2")
