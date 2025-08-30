nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print('Sua média é {}, você está reprovado.'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média é {}, você está de recuperação.'.format(media))
else:
    print('Sua média é {}, você está aprovado.'.format(media))
