jogadores = []
total_jogadores = 0
int(input('Insira o total de jogadores'))

for jogador in jogadores:
    jogadores[0]['nome'] = int(input('Insira o nome do primeiro jogador'))
    jogadores[0]['pontuacao'] = int(input('Insira a pontuação do primeiro jogador'))
    jogadores[1['nome'] = int(input('Insira o nome do segundo jogador'))
    jogadores[1]['pontuacao'] = int(input('Insira a pontuação do segundo jogador'))

for jogador in jogadores:
    print('Jogador: ',jogador.get('nome'), 'Pontuação: ', jogador.get('pontuacao'))