import random

print('Tente advinhar o número que a máquina pensou!')
num = int(input('Digite um numero entre 0 e 5: '))
random = random.randrange(6)
if num == random:
    print('Você acertou!')
else:
    print('Você errou! Tente novamente.')
    print('O número pensado foi {}.'.format(random))