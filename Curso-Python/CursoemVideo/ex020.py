'''import random
nomes = ['João', 'Pedro' , 'Caio', 'Felipe']
random.shuffle(nomes)
print('A lista dos alunos sorteados em ordem é: {}'.format(nomes))'''

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem dos escolhidos foi {}.'.format(alunos))