import random
import time

jogos = {}

for j in range(4):
    jogador = f'Jogador{j+1}'
    jogos[jogador] = f'Jogador{j+1}'

    dado = f'dado{j+1}'
    jogos[dado] = random.randint(1,6)

    print(f'O {jogos[f'Jogador{j+1}']} tirou {jogos[f'dado{j+1}']}')
    time.sleep(1)

maior = jogos['dado1']
vencedor = jogos['Jogador1']
for i in range(2,5):
    if jogos[f'dado{i}'] > jogos['dado1']:
        maior = jogos[f'dado{i}']

print(maior)
print('Ranking dos jogadores')