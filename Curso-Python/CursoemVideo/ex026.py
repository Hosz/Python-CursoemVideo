frase = str(input('Digite uma frase: ')).lower().strip()
min = frase.count('a')
print('A frase possui {} letras "a".'.format(min))
comeco = frase.find('a')+1
final = frase.rfind('a')+1
print('A letra "A" aparece pela primeira vez em {} e pela ultima em {}.'.format(comeco, final))