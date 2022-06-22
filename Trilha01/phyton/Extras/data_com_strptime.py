import datetime
str_data = input("Informe sua data de nascimento no formato DD-MM-YYYY")

#Metodo strptime cria uma variavel datetime baseando-se em um texto(variavel str_data)
dt_nascimento = datetime.datetime.strptime(str_data, "%d-%m-%Y")

#Exibe a data no formato desejado Dia + / + Mes + / + Ano(%d/%m/%Y) Atenção ao Y em maiúsculo para não abreviar o ano
print(40*'-')
print(f"A data de nascimento é: {dt_nascimento.strftime('%d/%m/%Y')}")
print(40*'-')
