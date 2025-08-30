def perimetro(a, b):
    p = (a * b)
    print(f'O terreno de {a} por {b} tem uma área de {p}m².')


a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
perimetro(a, b)