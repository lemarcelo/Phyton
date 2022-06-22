import datetime
str_data = input('Informe a data no formato DD-MM-YYYY')

#Divisão da data em variáveis que compõem a data
ano, mes, dia = map(int, str_data.split('-'))
data_formatada = datetime.date(dia, mes, ano)

#Exibe a data no formato desejado Dia + / + Mes + / + ano(%d/%m/%Y) *\n é quebra de linha*
print(40*'-')
print(f"Esta é a data informada\n{data_formatada.strftime('%d/%m/%Y')}")
print(40*'-')
