print(40*'-')
pessoas = []
total_pessoas = int(input('Quantas pessoas deseja cadastrar'))
while len(pessoas) < total_pessoas:
    pessoas.append(input('Nome: '))
    print('Pessoa Adicionada')
print(40*'-')

print(f'LISTAGEM DE PESSOAS')
for pessoa in sorted(pessoas):
    print(f'{pessoa.title()}')