def notas(*num, sit=False):
    '''
    Função para analisar as notas e situações dos alunos.
    :param num: Uma ou mais notas do aluno (aceita varias).
    :param sit: Valor opcional, indicando se quer ou não ver a situação
    :return: Dicionario com varias informações sobre a situação da turma
    '''
    notas = {}
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num) / notas['total']
    if sit:
        if notas['media'] >= 7:
            notas['situação'] = 'BOA'
        elif 7 > notas['media'] == 6:
            notas['situação'] = 'Razoável'
        else:
            notas['situação'] = 'RUIM'
    return notas

r1 = notas(5.5, 9.5, 10, 6.5, sit=True)
print(r1)