from datetime import date
data_nascimento = date(1982, 12, 3)
hoje = date.today()
hoje = hoje.replace(day = 30)
print(data_nascimento.strftime('%d/%m/%Y'))
print(hoje.strftime('%d/%m/%Y'))