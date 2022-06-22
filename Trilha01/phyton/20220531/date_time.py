from datetime import datetime

antiga = datetime(2000, 11, 28, 14, 30, 25)
agora = datetime.now()


#print(f'Hoje é:{antiga.date()} e horario: {antiga.time()}')

print((agora - antiga).days)