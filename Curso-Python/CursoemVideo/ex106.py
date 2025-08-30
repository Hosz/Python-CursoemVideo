def menu(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(msg.center(tamanho))
    print('~' * tamanho)
def ajuda(args):
    return help(arg)

while True:
    menu('SISTEMA DE AJUDA PyHELP')
    arg = input('Função ou biblioteca: ')
    if arg == 'fim':
        menu('Até logo!')
        break
    ajuda(arg)


