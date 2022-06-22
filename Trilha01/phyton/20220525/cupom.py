print(20*'-','Valor da compra', 20*'-')
valor_compra = float(input('Insira o valor da compra'))
cupom = input('Insira o cupom de desconto').upper().replace(' ', '')

if cupom == 'CUPOM10':
    print(f'O valor do produto com desconto é R${round(valor_compra - (valor_compra * 0.1), 2)}')
    print(20*'-','Fim', 20*'-')
elif cupom =='CUPOM25':
    print(f'O valor do produto com desconto é R${round(valor_compra - (valor_compra * 0.25), 2)}')
    print(20*'-','Fim', 20*'-')
else:
    print('Este cupom não é valido')