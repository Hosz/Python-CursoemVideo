idades = 0
idadevelho = 0
nomevelho = 0
idademulher = 0
for c in range(1,5):
    print('-=-=-={} Pessoa=-=-=-'.format(c))
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Sexo [H/M] '))
    idades += idade
    if c == 1 and sexo in 'Hh':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Hh' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade < 20:
        idademulher += 1
print('A média de idade é de {:.0f} anos.'.format(idades / 4))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, idadevelho))
print('Tem apenas {} mulheres com menos de 20 anos.'.format(idademulher))