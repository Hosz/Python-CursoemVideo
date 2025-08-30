sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o seu sexo? ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Tente novamente.')
print('Fim')