nome_do_produto = input('Informe o nome do produto')
preco_de_custo = float(input('Informe o preço de custo do produto'))
taxa_de_imposto = float(input('Informe a alíquota de imposto %'))

def calcula_imposto():
    try:
        valor_imposto = (taxa_de_imposto / 100) * preco_de_custo
        return valor_imposto
        print(f'{valor_imposto}!!!!!!!!')
    except:
        print('Você precisa informar algum valor')
    finally:
        print('Algo deu errado')
        
print('\n Resultado: ')
print(f'Nome do produto {nome_do_produto}')
print(f'Preço de custo: R${preco_de_custo}')

print(f'Valor do imposto: R${calcula_imposto()}')
print(f'Valor total do produto: R${round(calcula_imposto())}')