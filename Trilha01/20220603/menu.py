def mostrar_menu():
    print('\n***********************************************')
    print('***************** CALCULADORA *****************')
    print('***********************************************')
    print('Escolha a opção desejada')
    print('1) Somar')
    print('2) Subtração')
    print('3) Multiplicação')
    print('4) Divisão')
    print('5) Sair')
    return int(input('Opção: '))
    
def capturar_numeros():
    nr_1 = float(input('Informe o primeiro número: '))
    nr_2 = float(input('Informe o segundo número: '))
    return nr_1, nr_2
    
def sair(surpresa = ''):
    if surpresa == ' ':
        print(f"░░░░░░░░░░░█▀▀░░█░░░░░░"+
                "░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░"+
                "░░░░░░█░█░░░░░░░░░░▐░░░"+
                "░░░░░░▐▐░░░░░░░░░▄░▐░░░"+
                "░░░░░░█░░░░░░░░▄▀▀░▐░░░"+
                "░░░░▄▀░░░░░░░░▐░▄▄▀░░░░"+
                "░░▄▀░░░▐░░░░░█▄▀░▐░░░░░"+
                "░░█░░░▐░░░░░░░░▄░█░░░░░"+
                "░░░█▄░░▀▄░░░░▄▀▐░█░░░░░"+
                "░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░"+
                "░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░"+
                "░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░"+
                "░░░░░░░░░░░░░░░░░░░░░░░\n')
    else:
        exit()