import time
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n = int(0)
print('Analisando os números...')
time.sleep(1)
while n != 5:
    print('-=-=-=OPÇÕES=-=-=-\n'
          '[1]Somar\n'
          '[2]Multiplicar\n'
          '[3]Maior\n'
          '[4]Novos Números\n'
          '[5]Sair do programa')
    n = int(input('O que deseja fazer? '))
    if n == 1:
        print('Somando...')
        soma = n1 + n2
        time.sleep(1.5)
        print('-=-'*20)
        print('A soma entre {} e {} é igual à {}.'.format(n1, n2, soma))
        print('-=-'*20)
        print('Aguarde alguns segundos...')
    if n == 2:
        print('multiplicando...')
        mult = n1 * n2
        time.sleep(1.5)
        print('-=-'*20)
        print('A multiplicação entre {} e {} é igual à {}'.format(n1, n2, mult))
        print('-=-'*20)
    if n == 3:
        print('Analisando...')
        time.sleep(1.5)
        if n1 == n2:
            print('-=-' * 20)
            print('Os dois números são iguais')
            print('-=-' * 20)
        else:
            maior = max(n1,n2)
            print('-=-'*20)
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
            print('-=-'*20)
    if n == 4:
        print('Aguarde alguns segundos...')
        time.sleep(1.5)
        print('-=-'*20)
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
        print('-=-'*20)
        print('Aguarde alguns segundos...')
    if n == 5:
        print('==='*20)
        print('Aguarde alguns segundos...')
    else:
        print('-=-'*20)
        print('Opção inválida. Tente novamente.')
        print('-=-'*20)
    time.sleep(2)

print('O programa foi encerrado.')