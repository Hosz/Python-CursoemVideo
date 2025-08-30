c = 'S'
count = soma = media = n = 0
lista = []
while c in 'Ss':
    n = int(input('Digite um número '))
    p = str(input('Deseja continuar?[S/N] ')).strip()[0]
    c = p
    count += 1
    soma += n
    media = soma / count
    lista.append(n)
maior = max(lista)
menor = min(lista)
print('Você digitou {} números e a média foi {}'.format(count, media))
print('O maior número foi {} e o menor foi {}.'.format(maior, menor))
