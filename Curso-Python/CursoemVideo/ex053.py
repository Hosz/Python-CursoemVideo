frase = input('Digite uma frase ').strip().lower().split()
frase2 = "".join(frase)
print(frase2, frase2[::-1])
if frase2 == frase2[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')