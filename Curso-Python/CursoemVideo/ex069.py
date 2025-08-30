maior = homem = muie = 0
while True:
    print('-'*41)
    print(f"{'CADASTRE UMA PESSOA':^40}")
    print('-'*41)
    while True:
        idade_str = input('Idade: ')
        if idade_str.isdigit():
            idade = int(idade_str)
            break
    while True:
        sexo = str(input('Sexo [M/F] ')).strip().lower()[0]
        if sexo in ('m','f'):
            break
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar == 's':
            break
        if continuar == 'n':
            break
    if idade > 18:
        maior += 1
    if sexo == 'm':
        homem += 1
    if sexo in 'f' and idade < 20:
        muie += 1
    if continuar == 'n':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos = {maior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {muie} mulheres com menos de 20 anos')