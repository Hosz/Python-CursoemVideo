import datetime
anos = int(input('Informe o ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - anos
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 10 <= idade <= 14:
    print('Sua categoria é INFANTIL.')
elif 15 <= idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif 20 == idade:
    print('Sua categoria é SÊNIOR.')
elif 21 <= idade:
    print('Sua categoria é MASTER.')