def linhas(qntd):
    print('-' * qntd)
def titulo(msg):
    linhas(50)
    print(msg.center(50))
    linhas(50)

def menuPrincipal(msg):
    linhas(50)
    print(msg.center(50))
    linhas(50)
    print(
        '\033[1;93m1\033[m - \033[036mVer pessoas cadastradas\033[m\n'
        '\033[1;93m2\033[m - \033[036mCadastrar nova pessoa\033[m\n'
        '\033[1;93m3\033[m - \033[036mSair do sistema\033[m'
    )
    linhas(50)

def leiaInt(op):
    while True:
        try:
            opt = input(op)
            if opt == '':
                opt = 0
                check = int(opt)
            check = int(opt)
        except (ValueError, TypeError):
            print('\033[031mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print('\033[031mERRO! O usuário não selecionou uma opção.\033[m')
            return 0
        else:
            return check

def pessoasCadastradas():
    titulo('PESSOAS CADASTRADAS')
    try:
        with open('Cadastro_Pessoas.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
            if not conteudo:
                print('Nenhuma pessoa cadastrada ainda.')
            else:
                print(conteudo)
    except FileNotFoundError:
        print('Nenhuma pessoa foi encontrada.')

def cadastrarPessoa():
    titulo('NOVO CADASTRO')
    nome = str(input('Nome: ')).strip()
    if nome == '':
        nome = '<Desconhecido>'
    checkIdade = leiaInt('Idade: ')
    idade = checkIdade
    with open('Cadastro_Pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome:<30}{idade:>5} anos\n')