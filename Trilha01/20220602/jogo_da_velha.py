matriz = [
        ['O', 'O', 'O'],
        ['X', 'X', 'O'],
        ['X', 'O', 'O']
    ]
#Método para executar o jogo
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
        for linha in matriz:
    print(linha)
            
    elif(matriz[0][0]=='O' and matriz[0][1]=='O' and matriz[0][2]=='O' or \
        matriz[1][0]=='O' and matriz[1][1]=='O' and matriz[1][2]=='O' or \
        matriz[2][0]=='O' and matriz[2][1]=='O' and matriz[2][2]=='O' or \
        
        matriz[0][0]=='O' and matriz[1][0]=='O' and matriz[2][0]=='O' or \
        matriz[0][1]=='O' and matriz[1][1]=='O' and matriz[2][1]=='O' or \
        matriz[0][2]=='O' and matriz[1][2]=='O' and matriz[2][2]=='O' or \
        
        matriz[0][0]=='O' and matriz[1][1]=='O' and matriz[2][2]=='O' or \
        matriz[0][2]=='O' and matriz[1][1]=='O' and matriz[2][0]=='O'):
        print('O Ganhou')
        print(
            f'{matriz[0]}\n'+
            f'{matriz[1]}\n'+
            f'{matriz[2]}')
jogo_da_velha()
#matriz[1][1] = 8