'''import random
a1 = 'João', 'Pedro' , 'Caio', 'Felipe'
print('O aluno sorteado pelo professor foi: {}!'.format(random.choice(a1)))'''

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi {}!'.format(escolhido))