import time
play = input('Digite "play": ').lower().strip()
print('O estouro de fogos vai começar em: ')
if play == 'play':
    for play in range(10, -1, -1):
        time.sleep(1)
        print(play)
print('Começou os fogos!!')