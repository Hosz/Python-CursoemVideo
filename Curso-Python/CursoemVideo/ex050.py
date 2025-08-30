soma = 0
for n in range(6):
    x = int(input('Digite um número '))
    if x % 2 == 0:
        soma += x
print('A soma dos números pares citados acima é de {}.'.format(soma))