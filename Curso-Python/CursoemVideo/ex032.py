from datetime import date
print('Descubra se o ano é bissexto.')
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
bs = ano % 4
if bs == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))