print('Descubra o valor da viagem abaixo.')
viagem = int(input('Quantos KM foram rodados na viagem? '))
abaixo = 0.50
acima = 0.45
if viagem <= 200:
    print('O valor da viagem será de R${:.2f}.'.format(viagem * abaixo))
else:
    print('O valor da viagem será de R${:.2f}.'.format(viagem * acima))
