r: str = input('Digite um valor: ')
print('Qual é o tipo primitivo desse valor?',type(r))
(print('Ele é maiúsculo? {};'.format(r.isupper())),
   print('Ele é numérico? {};'.format(r.isnumeric())),
      print('Ele é alfanumérico? {};'.format(r.isalnum())),
            print('Ele é alfabetico? {};'.format(r.isalpha())),
                  print('Ele é um ASCII? {};'.format(r.isascii())),
                        print('Ele é um decimal? {};'.format(r.isdecimal())),
                              print('Ele é um digito? {};'.format(r.isdigit())),
                                    print('Ele é: {};'.format(r.isidentifier())),
                                          print('Ele é minusculo? {};'.format(r.islower())),
                                                print('Ele é impresso? {};'.format(r.isprintable())),
                                                      print('Ele é: {};'.format(r.isspace())),
                                                            print('Ele é: {}.'.format(r.istitle())))