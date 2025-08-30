n = int(input('Quantos numeros da sequencia você quer que apareça? '))
s = n
n1 = 0 #primeiro numero
n2 = 1 #segundo numero
cont = 0 #contador
mais = n #numero de sequencia
total = 0 #variavel de soma
while mais != 0: #enqt "mais" for diferente de 0 vai rodar tudo
    total += mais #variavel de soma + o numero de sequencia
    while cont < total: #contador = 0 for diferente do total = variavel de soma + a qntd da sequencia
        print('{} >'.format(n1),end=' ')
        proximo = n1 + n2 #calculo do proximo
        n1 = n2 #o segundo valor será o primeiro
        n2 = proximo #o resultado da soma vai ser o segundo
        cont += 1 #vai ficar adicionando ao contador ate chegar no valor total
    print('Pausa')
    mais = int(input('\nQuantos numeros quer adicionar a sequencia? '))
print('fim')