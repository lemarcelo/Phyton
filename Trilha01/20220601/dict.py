tabela_preco = {
    'standard': {'adulto':120, 'crianca': 60},
    'luxo': {'adulto':180, 'crianca': 90}
}
#print(tabela_preco.get('standard').get('adulto'))
##No exemplo abaixo caso não tenha uma das chaves dará erro, o contrário da opção de cima
#print(tabela_preco['standard']['adulto'])
print(tabela_preco.get('luxo').get('crianca'))
