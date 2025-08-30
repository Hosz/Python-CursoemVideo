print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
for i in range(0, len(lista), 2):
    produto = lista[i]
    preço = lista[i + 1]
    print(f'{produto:.<30}R$ {preço:>7.2f}')
print('-'*40)