nome = str(input('Digite seu nome: '))
div = nome.split()
print('''Nome: {}
Primeiro Nome: {}
Ultimo Nome: {}
'''.format(nome, div[0], div[-1]))