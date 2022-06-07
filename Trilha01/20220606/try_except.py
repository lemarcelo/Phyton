#print(4/0)
try:
    nr_1 = int(input('Digite primeiro número: '))
    nr_2 = int(input('Digite o segundo número: '))
    print(f'Número 1 dividido por {nr_1} / {nr_2}  = {nr_1/nr_2}')

except ZeroDivisionError:
    print('Você não pode dividir um número por 0!')
except:
    print('Você precisa digitar um número!')
else:
    print('Todas as entradas estão corretas e o processamento foi realizado')
finally:
    print('Sempre vou executar')