count = 0
while True:
    n = int(input('Qual tabuada deseja ver? '))
    if n >= 0:
        t = f'Tabuada de {n}'
        print('='*41)
        print(f'{t:^40}')
        print('='*41)
        while True:
            count += 1
            resultado = n * count
            print(f'''{n} x {count} = {resultado}''')
            if count == 10:
                count = 0
                break
        print('='*41)
    else:
        print('='*41)
        print('PROGRAMA ENCERRADO.')
        print('='*41)