km = int(input('Quantos KM estava o carro? '))
multa = float(7.00)
acima = km - 80
if km <=80:
    print('O carro estava no limite aceitável.')
    print('Não há multa à ser paga.')
else:
    valor = acima * multa
    print('O carro estava acima do limite permitido.')
    print('O proprietário pagará um valor de {} pela multa.'.format(valor))