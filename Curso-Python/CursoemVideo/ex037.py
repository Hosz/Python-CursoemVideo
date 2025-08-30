numero = int(input('Digite um número: '))
print("Para qual método quer converter?\n"
      "Digite [1] para BINÁRIO \n"
      "Digite [2] para HEXADECIMAL \n"
      "Digite [3] para OCTAL \n")
way = int(input('Sua opção: '))
if way == 1:
    print('{} Convertendo para BINÁRIO é = {}'.format(numero, bin(numero)[2:]))
elif way == 2:
    print('{} Convertendo para HEXADECIMAL é = {}'.format(numero, hex(numero)[2:]))
elif way == 3:
    print('{} Convertendo para OCTAL é = {}'.format(numero, oct(numero)[2:]))
else:
    print('Opção inválida, tente novamente.')