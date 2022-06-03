matriz = [
        ['O', 'O', 'X'],
        ['X', 'X', 'O'],
        ['X', 'O', 'O']
    ]

    a = input('Jogador 1 informe a posição Numero da colula - Numero da linha(0-0 ou 1-1)')
    
    matriz[a[0]][a[1]]

    b = input('Jogador 2 informe a posição Numero da colula - Numero da linha(0-0 ou 1-1)')



    jogo_da_velha()



def jogo_da_velha():
    if (matriz[0][0]=='X' and matriz[0][1]=='X' and matriz[0][2]=='X' or \
        matriz[1][0]=='X' and matriz[1][1]=='X' and matriz[1][2]=='X' or \
        matriz[2][0]=='X' and matriz[2][1]=='X' and matriz[2][2]=='X' or \
        
        matriz[0][0]=='X' and matriz[1][0]=='X' and matriz[2][0]=='X' or \
        matriz[0][1]=='X' and matriz[1][1]=='X' and matriz[2][1]=='X' or \
        matriz[0][2]=='X' and matriz[1][2]=='X' and matriz[2][2]=='X' or \
        
        matriz[0][0]=='X' and matriz[1][1]=='X' and matriz[2][2]=='X' or \
        matriz[0][2]=='X' and matriz[1][1]=='X' and matriz[2][0]=='X'):
        print('X Ganhou')
        print(
            f'{matriz[0]}\n'+
            f'{matriz[1]}\n'+
            f'{matriz[2]}')



#matriz[1][1] = 8