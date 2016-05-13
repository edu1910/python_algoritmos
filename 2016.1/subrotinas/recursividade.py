def fatorial(num):
    if num <= 1:
        return 1
    return num*fatorial(num-1)

num = int(input('Digite um número inteiro: '))
print('Fatorial =', fatorial(num))

#fat = num

#if num == 0:
    #fat = 1

#for i in reversed(range(1, num)):
    #fat = fat * i

#print('Fatorial =', fat)

