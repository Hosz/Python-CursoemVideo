pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
ptermo = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(ptermo), end='')
        ptermo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja? '))
print('Acabou')