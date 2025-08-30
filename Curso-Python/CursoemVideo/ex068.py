import random
count = 0
print('=-' * 41)
print('Jogo do PAR ou IMPAR')
print('=-' * 41)
while True:
    n = int(input('Diga um valor: '))
    x = str(input('Par ou Impar? [P/I] ')).strip().lower()[0]
    while x not in ('p', 'i'):
        x = str(input('Par ou Impar? [P/I] ')).strip().lower()[0]
    pc = random.randint(0,10)
    soma = n + pc
    print('-'*41)
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {soma} DEU PAR!')
        print('-'*41)
    else:
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {soma} DEU IMPAR!')
        print('-'*41)
    if x in 'Pp' and soma % 2 == 0:
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
        count += 1
    elif x in 'Ii' and soma % 2 != 0:
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
        print('-='*41)
        count += 1
    else:
        print('Você PERDEU!')
        print('-='*41)
        break
print(f'GAME OVER! Você venceu {count} vezes.')