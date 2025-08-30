print('Gostaria de um empréstimo bancário para à compra de um imóvel?')
ValorCasa = float(input('O valor da casa é de: '))
anos = int(input('Quantos anos planeja pagar a casa? '))
salario = float(input('Qual é o valor do seu salário? '))
mensalidade = anos * 12
prestação = ValorCasa / mensalidade
if prestação > (salario * 0.30):
    print('Você não pode obter esse empréstimo pois tem um salário abaixo de 30% do valor da prestação.')
else:
    print('Dadas informações passadas, é possível a aquisição do empréstimo.')