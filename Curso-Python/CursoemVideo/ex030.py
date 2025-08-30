print('Descubra se um número é impar ou par.')
num = int(input('Digite um número: '))
cal = num / 2
resto = cal % 1
if resto == 0:
    print('O número {} é um número par.'.format(num))
else:
    print('O número {} é um número impar.'.format(num))