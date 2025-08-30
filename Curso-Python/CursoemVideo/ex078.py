num = list()
mai = 0
men = 0
for p in range(0,5):
    num.append(int(input('Digite um valor: ')))
    if p == 0:
        mai = men = num[p]
    else:
        if num[p] > mai:
            mai = num[p]
        if num[p] < men:
            men = num[p]
print(f'Os valores digitados foram: {num}')
print(f'Sendo o maior sendo ({max(num)}) e o menor sendo ({min(num)}).')
print(f'Estando o maior na(s) posição(ões):', end=' ')
for i, v in enumerate(num):
    if v == mai:
        print(i, end='; ')
print(f'\nEstando o menor na(s) posição(ões):', end=' ')
for i, v in enumerate(num):
    if v == men:
        print(i, end='; ')