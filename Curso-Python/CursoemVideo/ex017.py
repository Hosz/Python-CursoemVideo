import math
x = float(input('Digite o valor de um cateto: '))
y = float(input('Digite o valor de outro cateto: '))
'''z = pow(x, 2) + pow(y, 2)
h = math.sqrt(z)'''
h = math.hypot(x, y)
print('O valor da hipotenusa é igual à {:.2f}'.format(h))