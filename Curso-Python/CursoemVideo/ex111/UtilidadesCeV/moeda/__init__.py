


def aumentar(n, x, moeda=True):
    v = (x / 100) * n
    v += n
    if moeda:
        if moeda is True:
            v = f'R${v:.2f}'
    return v

def diminuir(n, x, moeda=True):
    v = (x / 100) * n
    n -= v
    if moeda:
        if moeda is True:
            n = f'R${v:.2f}'
    return n

def dobro(n, moeda=True):
    v = n * 2
    if moeda:
        if moeda is True:
            v = f'R${v:.2f}'
    return v

def metade(n, moeda=True):
    v = n / 2
    if moeda:
        if moeda is True:
            v = f'R${v:.2f}'
    return v

#def moeda(n):
    #return f'R${n:.2f}'

def resumo(n, aumento, reducao):
    aumentos = aumentar(n, aumento)
    reducoes = diminuir(n, reducao)
    meio = metade(n)
    dobrar = dobro(n)
    msg = 'RESUMO DO VALOR'
    print('-' * (30 + 2))
    print(msg.center(30 + 2))
    print('-' * (30 + 2))
    print(f'Preço analisado:     R${n:.2f}\n'
          f'Dobro do preço:      {dobrar}\n'
          f'Metade do preço:     {meio}\n'
          f'{aumento}% de aumento:      {aumentos}\n'
          f'{reducao}% de redução:      {reducoes}\n')
    print('-' * (30 + 2))