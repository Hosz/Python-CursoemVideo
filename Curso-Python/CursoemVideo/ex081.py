n = list()
while True:
    p = int(input('Digite um número: '))
    n.append(p)
    p2 = input('Deseja continuar?[S/N] ').lower()
    if p2 in 'n':
        break
print(f'{len(n)} números foram digitados.')
print(f'Em ordem decrescente a lista ficou assim: {sorted(n,reverse=True)}')
if 5 in n:
    print(f'O número 5 se encontra na posição {n.index(5)+1}.')
else:
    print('O número 5 não se encontra na lista.')