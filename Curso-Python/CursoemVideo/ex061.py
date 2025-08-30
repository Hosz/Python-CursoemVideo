pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
ptermo = pt
while cont <= 10:
    print('{} > '.format(ptermo), end='')
    ptermo += r
    cont += 1
print('Acabou')