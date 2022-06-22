from datetime import date, datetime, datetime, timedelta

dt_assinatura = date(2022, 5, 31)


dt_renovacao = dt_assinatura + timedelta(days = 30)

print(f"Assinatura expira em: {dt_assinatura.strftime('%d/%m/%Y')}")