def leiaInt(msg):
    while True:
        try:
            num = str(input(msg))
            v = int(num)
        except ValueError:
            print(f'ERRO! Digite um valor inteiro válido.')
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não informar um número.')
            return 0
        else:
            return v

def leiaFloat(msg):
    while True:
        try:
            num = input(msg)
            v = float(num)
        except (ValueError, TypeError):
            print(f'ERRO! Digite um número real válido.')
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não informar um número real.')
            return 0
        else:
            return v