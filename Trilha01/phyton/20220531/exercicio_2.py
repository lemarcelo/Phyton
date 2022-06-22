from datetime import datetime, date
nome = input('\nInforme seu nome:')
str_data = input('Informe a data de nascimento no formato DD/MM/AAAA')

dt_nascimento = datetime.strptime(str_data, '%d/%m/%Y')
idade = ((date.today() - dt_nascimento.date()) / 365).days

if idade >= 21:
    print(f'{nome} tem {idade} e é de maior')
else:
    print(f'{nome} tem {idade} e é de menor')
