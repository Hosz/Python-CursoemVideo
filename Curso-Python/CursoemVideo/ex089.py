alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno = [nome, [nota1, nota2], media]
    alunos.append(aluno)
    p = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    while p not in 'sn':
        p = str(input('Opção inválida... Tente novamente.\n'
                      'Deseja continuar? [S/N] ')).strip().lower()[0]

    if p in 'n':
        print('-=' * 30)
        print(f'{"Nº":^3} {"NOME":^10} MÉDIA')
        print('-' * 30)
        for i, aluno in enumerate(alunos):
            print(f'{i:^3} {aluno[0].title():^10} {aluno[2]:.1f}')
        while True:
            print('-' * 30)
            cont = int(input('Deseja ver a nota de qual aluno?: '))
            if cont == 999:
                break
            if cont <= len(alunos) - 1:
                print(f'Nota do(a) aluno(a) {alunos[cont][0]} é {alunos[cont][1]}.')
        break

print('-' * 30)
