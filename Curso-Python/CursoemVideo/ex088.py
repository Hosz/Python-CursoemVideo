import random

n = int(input('Quantos jogos você quer gerar?: '))
jogos = []
for i in range(0, n):
    jogo = []
    while len(jogo) < 6:
        x = random.randint(1,60)
        if x not in jogo:
            jogo.append(x)
        if len(jogo) == 6:
            jogos.append(jogo)
for ind, j in enumerate(jogos):
    print(f'Jogo[{(ind)+1}]: {j}')