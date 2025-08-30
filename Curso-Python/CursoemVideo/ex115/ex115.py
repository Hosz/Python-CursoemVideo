import time
import mods
while True:
    mods.menuPrincipal('MENU PRINCIPAL')
    op = mods.leiaInt('\033[1;92mSua opção:\033[m ')
    if op == 1:
        mods.pessoasCadastradas()

    elif op == 2:
        mods.cadastrarPessoa()

    elif op == 3:
        mods.titulo('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')

    time.sleep(1.5)