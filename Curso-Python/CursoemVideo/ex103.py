def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    return f'O jogador {nome.title()} fez {gols} gol(s) no campeonato.'

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

r1 = ficha(nome, gols)
print(r1)