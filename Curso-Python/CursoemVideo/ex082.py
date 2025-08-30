numeros = list()
pares = list()
impares = list()
while True:
    p = int(input('Digite um número: '))
    numeros.append(p)
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
    p2 = input('Quer continuar?[S/N] ').lower().strip()[0]
    while p2 not in 'sn':
        p2 = input('Quer continuar?[S/N] ').lower().strip()[0]
    if p2 in 'n':
        break
print(f'Números digitados: {numeros}.')
print(f'Números pares digitados: {pares}.')
print(f'Números ímpares digitados: {impares}.')