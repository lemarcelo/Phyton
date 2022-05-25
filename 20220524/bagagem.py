peso_bagagem = float(input('Informe o peso total da bagagem:'))

if peso_bagagem > 10:
    print(f'Necessário pagar R$ {round((peso_bagagem - 10) * 2, 3)} a mais pela bagagem\n {round(peso_bagagem - 10)}Kg exedidos')
else:
    print('Não é necessário pagar a mais pela bagagem')