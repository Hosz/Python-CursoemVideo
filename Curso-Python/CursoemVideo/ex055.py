pesos = []
for x in range(1,4):
    peso = float(input('Qual é o seu peso? '))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print('O maior peso é de {}Kg'.format(maior))
print('O menor peso é de {}Kg'.format(menor))