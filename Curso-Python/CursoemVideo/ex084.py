pessoas = list()
dados = list()
count = 0
maiores = list()
menores = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    count += 1

    x = str(input('Deseja continuar? [S/N] '))
    while x not in 'sn':
        x = str(input('Deseja continuar? [S/N] '))
    if x == 'n':
        break

maior = pessoas[0][1]
menor = pessoas[0][1]
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

for p in pessoas:
    if p[1] == maior:
        maiores.append(p[0])
    if p[1] == menor:
        menores.append(p[0])

print(f'Foram adicionadas {count} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {maiores}')
print(f'O menor peso foi de {menor}Kg. Peso de {menores}')