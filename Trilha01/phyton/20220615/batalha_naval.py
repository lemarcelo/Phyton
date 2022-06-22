from random import choice

opcoes = ['*', '']

batalha_naval = [
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
]

def jogo_batalha_naval():
    pontos = 0
    for jogada in range(0, 4):
        coluna = int(input('Informe de 0 a 4 coluna:'))
        linha = int(input('Informe de 0 a 3 linha:'))
        if batalha_naval[coluna][linha] == '*':
            pontos += 10
            print(f'Você acertou')
        else:
            pontos -= 10
            print(f'Você errou')
    return pontos
    
pontos = jogo_batalha_naval()
print(f'\n \n Placar final:\n{pontos} pontos')
