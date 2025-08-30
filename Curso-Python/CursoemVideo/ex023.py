num = int(input('Digite um valor: '))
#numero = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('''Número digitado: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num, u, d, c, m))
