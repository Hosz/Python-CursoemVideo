num = [[],[]]
for p in range(7):
    x = int(input('Digite um valor: '))
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)
print(f'Os valores pares foram: {sorted(num[0])}')
print(f'Os valores impares foram: {sorted(num[1])}')
