import time
def maior(*args):
    maior = 0
    for n in args:
        if n >= maior:
            maior = n
    print('Analisando valores passados...')
    for n in args:
        print(n, end=' ')
        time.sleep(.8)
    print(f'Foram informados {len(args)} valores ao todo.\n'
          f'O maior valor foi {maior}')

def linha():
    print('-='* 30)

linha()
maior(2, 9, 4, 5, 7, 1)

linha()
maior(4, 7, 0)

linha()
maior(1,2)

linha()
maior(6)

linha()
maior()
