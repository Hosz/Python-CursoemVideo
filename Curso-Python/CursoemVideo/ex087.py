matriz = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
pares = 0
soma = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]


for l in range(3):
    soma += matriz[l][2]

maior = max(matriz[1])

print('\nMatriz 3x3:')
for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^5}', end='')
    print()

print(f'Os numeros pares são: {pares}')
print(f'A soma dos numeros da terceira coluna: {soma}')
print(f'O maior valor da segunda linha: {maior}')