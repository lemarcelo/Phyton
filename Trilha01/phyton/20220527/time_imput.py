time_a = []
time_b = []

for i in (1, 3):
    nome = input('Nome:')
    nr_camisa = int(input('Camisa:'))
    if len(time_a) < 5:
        time_a.append({'nome': nome, 'nr_camisa': nr_camisa})
    elif len(time_b) < 5:
        time_b.append({'nome': nome, 'nr_camisa': nr_camisa})
print('Jogadores do time A:')
for jogador in time_a:
    print(jogador.get('nr_camisa'), jogador.get('nome'))
print('Jogadores do time B:')
for jogador in time_b:
    print(jogador.get('nr_camisa'), jogador.get('nome'))