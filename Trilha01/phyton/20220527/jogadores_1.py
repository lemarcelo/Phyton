jogadores = []
jogador_1 = {'nome': 'Matheus', 'pontuacao': 0}
jogador_2 = {'nome': 'Leandro', 'pontuacao': 0}

jogadores.append(jogador_1)
jogadores.append(jogador_2)

jogadores[0]['pontuacao'] = 10
jogadores[1]['pontuacao'] = 15

for jogador in jogadores:
    print('Jogador: ',jogador.get('nome'), 'Pontuação: ', jogador.get('pontuacao'))