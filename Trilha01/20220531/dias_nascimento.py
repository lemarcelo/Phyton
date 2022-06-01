from datetime import date

dt_1 = date(1995, 7, 7)
dt_2 = date(2022, 5, 31)
#dt_2 = dt_2.replace(year=2000, month=1)

diferenca = (dt_2 - dt_1) / 365

print(f'{diferenca.days}')
