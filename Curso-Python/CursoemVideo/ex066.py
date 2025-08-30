import time
w = count = soma = 0
while True:
    n = int(input('Digite um número [999 para parar] '))
    if n == 999:
        break
    soma += n
    count += 1
print('O programa foi finalizado.')
print('='*20)
time.sleep(1)
print(f'Você digitou {count} digitos.')
print(f'A soma dos números digitados foi de {soma}.')