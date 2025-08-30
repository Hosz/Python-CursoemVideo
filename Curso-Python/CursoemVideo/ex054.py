import datetime
hj = datetime.date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Qual o ano do seu nascimento?'))
    idade = hj - nasc
    if idade >= 18:
        maior += 1
        print('É de maior')
    else:
        menor += 1
        print('É de menor')
print('Apenas {} são de maior.'.format(maior))
print('Apenas {} são de menor.'.format(menor))