x1 = int(input('Digite um número: '))
x2 = int(input('Digite outro número: '))
x3 = int(input('Digite outro número: '))
x4 = int(input('Digite o último número: '))
x = (x1, x2, x3, x4)
count = x.count(9)
if 3 in x:
    where = x.index(3)
    print(f'O valor 3 está na {where + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado.')
print(f'O valor 9 apareceu {count} vezes')
par = tuple(num for num in x if num % 2 == 0)
print(f'Foram digitados os seguintes números pares: {par}')