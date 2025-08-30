print('Descubra quanto de aumento você terá.')
salario = float(input('Digite o seu salário: '))
if salario > 1250.00:
    print('Com o aumento de seu salário, você receberá {:.2f}.'.format((salario*0.10)+salario))
else:
    print('Com o aumento de seu salário, você receberá {:.2f}.'.format((salario*0.15)+salario))