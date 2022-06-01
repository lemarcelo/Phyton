from datetime import date, timedelta

dt_1 = date(2022, 5, 31)
dt_2 = date(2022, 12, 31)


dt_a = dt_1 + timedelta(days = 180)

print(f"Daqui 180 dias será : {dt_a.strftime('%d/%m/%Y')}")
print(f"Faltam: {(dt_2 - dt_1).days} dias para o Reveillon de 2022/2023")
