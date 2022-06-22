#Henrique bastos
nome = input('Digite seu nome')
idade = int(input(f'Digite sua Idade'))
caracteres_nome = len(nome)

if and idade >= 21:
    print(f'{nome.title()} é maior de idade')
else:
    print(f'{nome.title()} é menor de idade')
