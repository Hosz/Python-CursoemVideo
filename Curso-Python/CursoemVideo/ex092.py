import datetime

pessoa = {}

#nome da pessoa
pessoa['nome'] = input('Nome: ').title()

#Idade da pessoa
data = int(input('Data de nascimento: '))
pessoa['idade'] = datetime.date.today().year - data

#carteira de trabalho
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tem):'))

if pessoa['ctps'] == 0:
    print(f'Nome: {pessoa['nome']}\n'
          f'Idade: {pessoa['idade']} anos\n'
          f'CTPS: Inexistente.'
          )

elif pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))

    #Aposentadoria
    contribuição = datetime.date.today().year - pessoa['contratação']
    resto = 35 - contribuição
    pessoa['aposentadoria'] = resto + pessoa['idade']

    print(
        f'Nome: {pessoa['nome']}\n'
        f'Idade: {pessoa['idade']}\n'
        f'CTPS: {pessoa['ctps']}\n'
        f'Contratação: {pessoa['contratação']}\n'
        f'Salário: {pessoa['salário']:.2f}\n'
        f'Aposentadoria: {pessoa['aposentadoria']}'
    )