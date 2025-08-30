def voto(num):
    from datetime import date
    situação = 'Indefinida'
    atual = date.today().year
    idade = atual - num
    if 18 == idade <= 65:
        situação = 'Voto obrigatório'
    elif idade > 65:
        situação = 'Voto opcional'
    elif idade >= 16:
        situação = 'Voto opcional'
    else:
        situação = 'Não vota'

    return print(f'Com {idade}: {situação}')


n = int(input('Em que ano você nasceu? '))
r1 = voto(n)
