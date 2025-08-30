'''fatorial = 1
calculo = ''
n = int(input('Digite um valor para ter o fatorial: '))
for c in range(n, 0, -1):
    fatorial *= c
    if c > 1:
        calculo += '{} x '.format(c)
    else:
        calculo += '{} = '.format(c)
calculo += str(fatorial)
print('{}! = {}'.format(n, calculo))'''
from struct import calcsize

n = int(input('Digite o valor para ter o fatorial: '))
contador = n
fatorial = 1
calculo = ''
while contador > 0:
    fatorial *= contador
    contador -= 1
calculo += str(fatorial)
print(calculo)