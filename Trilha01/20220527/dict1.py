pessoa = {
    'nome':'',
    'idade': 0,
    'sexo': ''}
total_pessoas = int(input('Insira a quantidade de pessoas que deseja adicionar'))
if total_pessoas >= 1:
    for i in total_pessoas:
        pessoa['nome'] = input(f'Informe o nome da {i}ª pessoa')
        pessoa['idade'] = input(f'Informe a idade da {i}ª pessoa')
        pessoa['sexo'] = input(f'Informe o sexo da {i}ª pessoa')

print('Esta foi a pessoa adicionada')
print(f"{pessoa.get('nome')}")
print(f"{pessoa.get('idade')}")
print(f"{pessoa.get('sexo')}")