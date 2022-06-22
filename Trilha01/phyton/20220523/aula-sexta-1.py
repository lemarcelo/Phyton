print('CALCULO DE DESPESA DA VIAGEM')
valor_hospedagem = float(input('Valor diária uma pessoa'))
qtd_pessoas = int(input('Qual a quantidade de pessoas'))

valor_total_hospedagem = valor_hospedagem * qtd_pessoas

valor_pedagio = float(input('Valor do pedagio R$ '))
qtd_pedagios = int(input('Quantidade de pedagios: '))

valor_total_pedagio = valor_pedagio * qtd_pedagios

valor_litro_gasolina = float(input('Valor do litro da gasolina'))
distancia_total = float(input('Distância total da viagem'))
autonomia = float(input('Autonomia do veículo'))

valor_total_gasolina = (distancia_total / autonomia) * valor_litro_gasolina

valor_total_viagem = valor_total_hospedagem + valor_total_pedagio + valor_total_gasolina

print('CALCULO DE DESPESA DA VIAGEM')
print('Custo total da hospedagem: R$ ', round(valor_total_hospedagem, 2))
print('Custo total dos pedágios: R$ ', round(valor_total_pedagio, 2))
print('Custo total de combustível R$', round(valor_total_gasolina, 2))
print(40*'-')
print('VALOR TOTAL DA VIAGEM R$ ', round(valor_total_viagem, 2))