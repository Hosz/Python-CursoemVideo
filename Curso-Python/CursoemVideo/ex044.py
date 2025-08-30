valor = float(input('Valor do produto: '))
print('Formas de pagamento: \n-=-=(Dinheiro/Cheque)=-=-\n'
'-=-=(Cartão)=-=-')
pagamento = str(input('Qual é a forma de pagamento? ')).lower().strip()
if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('O valor a ser pago será de R${}.'.format(valor - (valor * 0.10)))#10% de desconto
elif pagamento == 'cartão':
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela == 1:
        print('O valor a ser pago será de {:.2f}.'.format(valor - (valor * 0.05)))#5% de desconto
    elif parcela == 2:
        print('O valor a ser pago será de R${:.2f}'.format(valor))#preço normal
    elif parcela >=3:
        print('O valor a ser pago será de R${:.2f}'.format(valor + (valor * 0.20)))#20% de juros