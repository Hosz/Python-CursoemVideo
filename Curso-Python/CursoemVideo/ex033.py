num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))
print('Números indicados: {}, {} e {}.'.format(num1, num2, num3))
if num1 > num2 and num1 > num3:
    print('{} é o maior.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('{} é o maior.'.format(num2))
else:
    print('{} é o maior.'.format(num3))

if num1 < num2 and num1 < num3:
    print('{} é o menor.'.format(num1))
elif num2 < num1 and num2 < num3:
    print('{} é o menor.'.format(num2))
else:
    print('{} é o menor.'.format(num3))