d = int(input('Por quantos dias foi alugado? '))
km = float(input('Quantos KM foi rodado? '))
d2 = d * 60
km2 = km * 0.15
print('O aluguel do carro ficou no valor de R${}'.format(d2 + km2))