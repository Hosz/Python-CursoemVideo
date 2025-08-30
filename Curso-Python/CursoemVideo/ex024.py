cidade = str(input('Digite o nome de uma cidade: '))
div = cidade.split()
up = div[0].upper()
santo = 'SANTO' in up
print(santo)