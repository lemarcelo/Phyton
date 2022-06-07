#print(4/0)
try:
    numero = int(input('Digite primeiro número: '))
    if numero < 10 or numero >20:
        raise Exception('Você digitou um numero fora da faixa exigida!')
        print(f'O dobro de {2*numero}')
except Exception as e:
    print(e)