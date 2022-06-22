from datetime import datetime
tabela_preco = {
    'standard': {'adulto':120, 'crianca': 60},
    'luxo': {'adulto':180, 'crianca': 90}
}
#print(tabela_preco.get('standard').get('adulto'))
##No exemplo abaixo caso não tenha uma das chaves dará erro, o contrário da opção de cima
#print(tabela_preco['standard']['adulto'])

tipo_hospedagem = input('Informe o tipo de hospedagem(luxo ou standard)').lower()
qtd_adultos = int(input('Informe a quantidade de adultos'))
qtd_criancas = int(input('Informe a quantidade de criancas'))
valor_frigobar = float(input('Informe o valor do frigobar').replace(',', '.'))
dt_checkin = datetime.strptime(input('Data Checkin DD-MM-AAAA'), '%d/%m/%Y')
dt_checkout = datetime.strptime(input('Data Chechout DD-MM-AAAA'), '%d/%m/%Y')

qtd_dias_hospedagem = (dt_checkout - dt_checkin).days
valor_total_adultos = qtd_adultos * qtd_dias_hospedagem * tabela_preco[tipo_hospedagem]['adulto']
valor_total_criancas = qtd_criancas * qtd_dias_hospedagem * tabela_preco[tipo_hospedagem]['crianca']
valor_total_hospedagem_pessoas = valor_total_adultos + valor_total_criancas
valor_total = valor_total_hospedagem_pessoas + valor_frigobar

print(f"{20*'-'}"+
    f"\nTipo de hospedagem: {tipo_hospedagem}"+
    f"\nQuantos Adultos: {qtd_adultos}"+
    f"\nQuantas crianças: {qtd_criancas}"+
    f"\nValor total dos adultos: R${round(valor_total_adultos)}"+
    f"\nValor Total das criancas: R${round(valor_total_criancas)}"+
    f"\nValor Frigobar: R${round(valor_frigobar)}"+
    f"\nDias da hospedagem: R${qtd_dias_hospedagem}"+
    f"\nTotal da hospedagem: R${round(valor_total_hospedagem_pessoas)}"+
    f"\n{20*'-'}")

forma_pagamento = input('Como voce deseja pagar [V] À vista ou [P] À prazo').lower()

if forma_pagamento == 'V':
    valor_desconto = valor_total * 0.15
    valor_pagamento = valor_desconto
    
elif forma_pagamento == 'P':
    valor_acrescimo = valor_total * 0.05
    valor_pagamento + valor_acrescimo
else:
    valor_pagamento = valor_total
    
print(f'Total de pagamentos R${round(valor_pagamento)}')
    
    
    