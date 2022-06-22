import os 
from time import sleep
from menu import mostrar_menu, capturar_numeros, sair
from ferramentas import soma, subtracao, multiplicacao, divisao
opcao = mostrar_menu()
print('Escolheu a opção: ', opcao)
while opcao != 5:
    nr_1, nr_2 = capturar_numeros()
    if opcao == 1:
        print(f'O resultado de {nr_1} + {nr_2} = {round(soma(nr_1, nr_2))}')
    elif opcao == 2:
        print(f'O resultado de {nr_1} - {nr_2} = {round(subtracao(nr_1,  nr_2))}')
    elif opcao == 3:
        print(f'O resultado de {nr_1} * {nr_2} = {round(multiplicacao(nr_1,  nr_2))}')
    elif opcao == 4:
        print(f'O resultado de {nr_1} / {nr_2} = {round(divisao(nr_1,  nr_2))}')
    elif opcao == 5:
        sair()
    else:
        print('Opção inválida')
    sleep(1)
    #os.system('clear')
    opcao = mostrar_menu()
print('Programa finalizado')