import time
import random
print('Vamos jogar jokenpo')
jogador = str(input('Escolha Pedra, Papel ou Tesoura: ')).lower().strip()
jogadas = ['pedra', 'papel', 'tesoura']
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('JOKENPO')
time.sleep(1.5)
pc = random.choice(jogadas)
print('Você jogou {}!'.format(jogador))
print('Eu joguei {}!'.format(pc))
if pc == 'papel' and jogador == 'pedra':
    print('Papel ganha de Pedra. Eu ganhei!!!')
elif pc == 'papel' and jogador == 'tesoura':
    print('Tesoura ganha de Papel. Você ganhou!!!')
elif pc == 'papel' and jogador == 'papel':
    print('Droga, empatamos... Boa sorte na proxima!')
elif pc == 'pedra' and jogador == 'tesoura':
    print('Pedra ganha de Tesoura. Eu ganhei!!!')
elif pc == 'pedra' and jogador == 'papel':
    print('Papel ganha de Pedra. Você ganhou!!!')
elif pc == 'pedra' and jogador == 'pedra':
    print('Droga, empatamos... Boa sorte na proxima!')
elif pc == 'tesoura' and jogador == 'papel':
    print('Tesoura ganha de Papel. Eu ganhei!!!')
elif pc == 'tesoura' and jogador == 'pedra':
    print('Tesoura perde pra pedra. Você ganhou!!!')
elif pc == 'tesoura' and jogador == 'tesoura':
    print('Droga,empatamos... Boa sorte na proxima!')
