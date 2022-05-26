valor_decimal = float(input('Insira um valor decimal'))

if valor_decimal <= 100:
    print(f'Valor de entrada vezes dois: {round(valor_decimal * 2, 3)}')
else:
    print(f'Valor de entrada mais mil: {round(valor_decimal + 1000, 3)}')