jogadores = []

while True:
    #Informações
    jogador = {}
    gols = []
    jogador['nome'] = str(input('Nome do jogador: ')).lower().strip().title()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for p in range(partidas):
        gol = int(input(f'Quantos gols na partida {p+1}? '))
        gols.append(gol)
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    #Continuação
    perg = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while True:
        if perg not in 'sn':
            perg = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().lower()[0]
        else:
            break
    if perg in 'n':
        break

#Tabela
print('-=' * 30)
print(f'{'COD':<5} {'NOME':<15} {'GOLS':<20} {'TOTAL':<10}')
print('-' * 60)

tamanho = len(jogadores)
for i in range(tamanho):
    jogador_atual = jogadores[i]
    nome = jogador_atual['nome']
    gols = str(jogador_atual['gols'])
    total = jogador_atual['total']

    print(f'{i+1:<5} {nome:<15} {gols:<20} {total:<10}')
print('-' * 60)

#dados de jogador especifico
while True:
    dados = int(input('Mostrar dados de qual jogador?: '))
    print('-' * 30)
    if dados == 999:
        break

    if dados - 1 >= tamanho or dados < 1:
        print('Esse jogador não existe.')
    else:
        jogador_selecionado = jogadores[dados - 1]
        print(f'-- Levantamento do Jogador {jogador_selecionado["nome"]}:')
        for i, gol in enumerate(jogador_selecionado['gols']):
            print(f'   No jogo {i+1} fez {gol} gols.')

print('-' * 40)
print('<<PROGRAMA ENCERRADO.>>')