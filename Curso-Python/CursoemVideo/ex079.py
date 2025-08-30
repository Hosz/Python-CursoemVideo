numeros = list()
stop = False
while stop is False:
    n = int(input('Digite um número: '))
    if n in numeros:
        print('Já tem.')
    else:
        numeros.append(n)
        print('Adicionei à lista.')
    p1 = input('Deseja continuar? [S/N] ').lower()
    if p1 in 'n':
        stop = True
print(f'Os números listados em ordem crescente foram: {sorted(numeros)}')