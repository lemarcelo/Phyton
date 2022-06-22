print('Calendário de temperaturas')
meses = [
    {'mes': 'Janeiro', 'temperatura': 31.5},
    {'mes': 'Fevereiro', 'temperatura': 30},
    {'mes': 'Março', 'temperatura': 19},
    {'mes': 'Abril', 'temperatura': 20},
    {'mes': 'Maio', 'temperatura': 16},
    {'mes': 'Junho', 'temperatura': 15},
    {'mes': 'Julho', 'temperatura': 19},
    {'mes': 'Agosto', 'temperatura': 25},
    {'mes': 'Setembro', 'temperatura': 28},
    {'mes': 'Outubro', 'temperatura': 29},
    {'mes': 'Novembro', 'temperatura': 28},
    {'mes': 'Dezembro', 'temperatura': 35}]
media_ano = 0
for mes in meses:
    media_ano += mes['temperatura']
    print(mes['mes'], "Temperatura média", mes['temperatura'])
    if mes['temperatura'] < 26:
        print('Calor')
    else:
        print('Frio')
print(40*'-')
print(f'Temperatura média do ano \n {media_ano / 12}')
print(40*'-')