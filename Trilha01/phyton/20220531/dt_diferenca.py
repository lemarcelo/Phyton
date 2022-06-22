from datetime import datetime

dt_1 = datetime(2022, 5, 31, 20, 42)
dt_2 = datetime(2024, 5, 31, 20, 42)

if dt_2 > dt_1:
    print(f'{dt_2.strftime("%d/%m/%Y")} é maior que {dt_1}')
else:
    print(f'{dt_1} é maior que {dt_2}')