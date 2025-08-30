jogador = {}
gols = []
count = 0

jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input('Quantas partidas ele jogou?: '))

#gols
for p in range(partidas):
    gol = int(input(f'Quantos gols ele fez na partida {p+1}?: '))
    gols.append(gol)
    count += 1

jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)

print(f'O jogador {jogador['nome'].title()} jogou {count} partidas.')
for p in range(partidas):
    print(f'   => Na partida {p+1}, fez {gols[p]} gols')
print(f'Com um total de {jogador['total']} gols.')