


def aumentar(n, x,formato=False ):
    v = (x / 100) * n
    v += n
    return v if not formato else moeda(v)

def diminuir(n, x,formato=False ):
    v = (x / 100) * n
    n -= v
    return n if not formato else moeda(n)

def dobro(n,formato=False ):
    v = n * 2
    return v if not formato else moeda(v)

def metade(n,formato=False):
    v = n / 2
    return v if not formato else moeda(v)

def moeda(n, mold='R$'):
    return f'{mold}{n:.2f}'.replace('.', ',')

def resumo(n, aumento, reducao):
    msg = 'RESUMO DO VALOR'
    print('-' * (30 + 2))
    print(msg.center(30 + 2))
    print('-' * (30 + 2))
    print(f'Preço analisado: \tR${n:.2f}\n'
          f'Dobro do preço: \t{dobro(n, formato=True)}\n'
          f'Metade do preço: \t{metade(n, formato=True)}\n'
          f'{aumento}% de aumento: \t{aumentar(n,aumento,formato=True)}\n'
          f'{reducao}% de redução: \t{diminuir(n,reducao,formato=True)}')
    print('-' * (30 + 2))