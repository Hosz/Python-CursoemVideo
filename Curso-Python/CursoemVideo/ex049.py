n = int(input('Digite o número que quer saber a taboada: '))
print('-='*21)
print('Taboada de {}'.format(n).center(40))
print('-='*21)
for x in range(1, 11):
    print('{} x {} = {}'.format(n, x, n * x))
print('-='*21)