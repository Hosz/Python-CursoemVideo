pessoa = {}
pessoas = []
media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while True:
        if pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    p = input('Você deseja continuar? [S/N] ').strip().lower()[0]
    while True:
        if p not in 'sn':
            p = input('Opção inválida. Deseja continuar? [S/N] ').strip().lower()[0]
        else:
            break
    if p in 'n':
        break

tamanho = len(pessoas)

#media
for p in pessoas:
    media += p['idade']
media = media / tamanho

#mulheres
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']

print('-=' * 30)
print(f'- O grupo tem {tamanho} pessoas')
print(f'- Média de idade é de {media:.2f} anos')

'''print(f'- Mulheres cadastradas: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']}; ',end='')'''

if mulheres:
    print(f'- Mulheres cadastradas: {", ".join(mulheres)}')
else:
    print(f'- Não há mulheres cadastradas.')
print()
print(f'- Lista de pessoas a cima da média:')
print()

for p in pessoas:
    if p['idade'] > media:
        print(f'Pessoa: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}')
        print()
print('<< ENCERRADO >>')
