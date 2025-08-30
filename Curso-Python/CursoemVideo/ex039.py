import datetime
idade = int(input('Digite o seu ano de nascimento: '))
data = datetime.date.today().year
if data - idade == 18:
    print('Está na hora de se alistar no Exército Brasileiro.')
elif data - idade < 18:
    print('Ainda vai chegar o seu tempo de se alistar no Exército Brasileiro.')
else:
    print('Já passou da hora de você se alistar.')