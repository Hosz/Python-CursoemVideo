aluno = {'nome': 'nome', 'media': 0.0, 'situação': 'situação'}
aluno['nome'] = input('Qual nome do aluno?: ')
aluno['media'] = float(input(f'Qual é a média de {aluno['nome'].title()}?: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(
    f'Aluno: {aluno['nome'].title()}\n'
    f'Média do aluno: {aluno['media']:.2f}\n'
    f'{aluno['nome'].title()} está {aluno['situação']}'
)