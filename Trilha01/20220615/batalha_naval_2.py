from random import choice

opcoes = ['*', '']

batalha_naval = [
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
]
pontos = 0

for jogada in range(0, 5):
    str_coordenada = input('Informe de 0 a 4 para a coluna e de 0 a 3 linha(Divididos por um -(hífem))')
    coluna = int(str_coordenada[0])
    linha = int(str_coordenada[2])
    if batalha_naval[coluna][linha] == '*':
        pontos += 10
        print(f'Você acertou')
    else:
        pontos -= 10
        print(f'Você errou')

print(f'Placar final:\n{pontos} pontos')
    

