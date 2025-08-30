peso = float(input('Digite seu peso: '))
altura = int(input('Digite sua altura em centimetros: '))
m = altura / 100
m2 = m ** 2
imc = peso / m2
print('Seu IMC é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif 18.6 <= imc <= 25:
    print('Você está no peso ideal.')
elif 25 <= imc <= 29.9:
    print('Você está com sobrepeso.')
elif 30 <= imc <= 39.9:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')