nome_menor = ''
preço_menor = preço_maior = soma = qntd = 0
cont = 1
while True:
    print('='*41)
    print(f'{f"Produto {cont}":^40}')
    print('='*41)
    nome = input('Nome do produto: ')
    preço = int(input('Valor do produto: R$ '))
    if preço_menor == 0 or preço < preço_menor:
        nome_menor = nome
        preço_menor = preço
    sel = ' '
    while sel not in 'sn':
        sel = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    cont += 1
    soma += preço
    if preço > 1000:
        preço_maior = preço
        qntd += 1
    if sel in 'n':
        break
print('='*41)
print(f'O gasto total das compras foi de R$ {soma}.')
print(f'Teve um total de {qntd} produtos acima de R$ 1000.')
print(f'O produto mais barato foi: {nome_menor}')