'''import math
ang = float((input('Digite um ângulo: ')))
print('O coseno desse ângulo é de {:.2f}.'.format(math.cos(math.radians(ang))))
print('O seno desse ângulo é de {:.2f}.'.format(math.sin(math.radians(ang))))
print('A tangente desse ângulo é de {:.2f}.'.format(math.tan(math.radians(ang))))'''
from math import cos, sin, tan, radians
ang = float(input('Digite o seu ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno de {} é {:.2f}'.format(ang, seno))
print('O cosseno de {} é {:.2f}'.format(ang, cos))
print('A tangente de {} é {:.2f}'.format(ang, tan))