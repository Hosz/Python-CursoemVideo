valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print('O valor {} é maior.'.format(valor1))
elif valor2 > valor1:
    print('O valor {} é maior.'.format(valor2))
else:
    print('Os dois valores são iguais.')