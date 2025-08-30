import random
import time
numeros = []

def sorteia():
    print(f'Sorteando os valores da lista: ', end='')
    for _ in range(5):
        aleatorios = random.randint(1,10)
        numeros.append(aleatorios)
        print(f'{aleatorios} ', end='', flush=True)
        time.sleep(0.5)

sorteia()
print()

def somaPar():
    numpar = []
    for n in numeros:
        if n % 2 == 0:
            numpar.append(n)
    print(f'Somando os valores pares de {numeros}, temos {sum(numpar)}.')

somaPar()