def leiaDinheiro(arg):
    ok = False
    while True:
        n = str(input(arg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO! "{n}" é um preço inválido.')
        else:
            n = float(n)
            ok = True
        if ok:
            break
    return n