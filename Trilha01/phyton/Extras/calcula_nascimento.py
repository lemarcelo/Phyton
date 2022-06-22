from datetime import date, datetime

str_data = input('Informe a data de nascimento no formato DD-MM-YYYY')

#Divisão da data em variáveis(que compõem a data) O que pe (map)?
dia, mes, ano = map(int, str_data.split('-'))
data_formatada = datetime.date(ano, mes, dia)

#Calcula a diferença em dias entre a data de nascimento e a data atual
def calculo_idade(param):
    return abs(datetime.datetime.now().date()-param).days#abs = absolut number - trás o número positivo independente do resultado

#Inicializa a execução da aplicação
def construtor():
    idade = calculo_idade(data_formatada)
    print(f"Você tem {round(idade / 365.2425)} anos")

construtor()