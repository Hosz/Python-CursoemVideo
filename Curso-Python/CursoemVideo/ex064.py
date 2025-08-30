n = count = soma = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar] '))
    count += 1
    soma += n
    if n == 999:
        soma -= 999
        count -= 1
print('Você digitou {} e a soma desses números deu {}.'.format(count, soma))