#Sortear primeiro
#from random import randint
matriz = [
        ['0-0', '0-1', '0-2'],
        ['1-0', '1-1', '1-2'],
        ['2-0', '2-1', '2-2']
    ]

#Dica de jogo
print(
        f'{matriz[0]}\n'+
        f'{matriz[1]}\n'+
        f'{matriz[2]}')
#Função que verifica resultado do jogo e 
def jogo_da_velha():
    #VERIFICAÇÃO SE O X GANHOU
    #HORIZONTAL
    if (matriz[0][0]=='|X|' and matriz[0][1]=='|X|' and matriz[0][2]=='|X|' or \
        matriz[1][0]=='|X|' and matriz[1][1]=='|X|' and matriz[1][2]=='|X|' or \
        matriz[2][0]=='|X|' and matriz[2][1]=='|X|' and matriz[2][2]=='|X|' or \
        #VERTICAL
        matriz[0][0]=='|X|' and matriz[1][0]=='|X|' and matriz[2][0]=='|X|' or \
        matriz[0][1]=='|X|' and matriz[1][1]=='|X|' and matriz[2][1]=='|X|' or \
        matriz[0][2]=='|X|' and matriz[1][2]=='|X|' and matriz[2][2]=='|X|' or \
        #DIAGONAL
        matriz[0][0]=='|X|' and matriz[1][1]=='|X|' and matriz[2][2]=='|X|' or \
        matriz[0][2]=='|X|' and matriz[1][1]=='|X|' and matriz[2][0]=='|X|'):
        print('X Ganhou')
        print(40*'-')
        print(
            f'{matriz[0]}\n'+
            f'{matriz[1]}\n'+
            f'{matriz[2]}')
        exit()
    #VERIFICAÇÃO SE O O GANHOU
    #HORIZONTAL
    elif (matriz[0][0]=='|O|' and matriz[0][1]=='|O|' and matriz[0][2]=='|O|' or \
        matriz[1][0]=='|O|' and matriz[1][1]=='|O|' and matriz[1][2]=='|O|' or \
        matriz[2][0]=='|O|' and matriz[2][1]=='|O|' and matriz[2][2]=='|O|' or \
        #VERTICAL
        matriz[0][0]=='|O|' and matriz[1][0]=='|O|' and matriz[2][0]=='|O|' or \
        matriz[0][1]=='|O|' and matriz[1][1]=='|O|' and matriz[2][1]=='|O|' or \
        matriz[0][2]=='|O|' and matriz[1][2]=='|O|' and matriz[2][2]=='|O|' or \
        #DIAGONAL
        matriz[0][0]=='|O|' and matriz[1][1]=='|O|' and matriz[2][2]=='|O|' or \
        matriz[0][2]=='|O|' and matriz[1][1]=='|O|' and matriz[2][0]=='|O|'):
        print('O Ganhou')
        print(40*'-')
        print(
            f'{matriz[0]}\n'+
            f'{matriz[1]}\n'+
            f'{matriz[2]}')
        exit()
    #VERIFICAÇÃO SE AS JOGADAS TERMINARAM
    else:
        #Variável de controle para contagem de jogadas
        controle = 0
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if matriz[linha][coluna] == '|O|' or matriz[linha][coluna] == '|X|':
                    controle += 1
                    if controle >= 9:
                        print(40*'-')
                        print(f'Os dois são bons, empagou!')
                        print(40*'-')
                        exit()
        #SEGUE O JOGO
        print(
            f'{matriz[0]}\n'+
            f'{matriz[1]}\n'+
            f'{matriz[2]}')

for jogadas in range(1,10):
    print(40*'-')
    str_posicao = input('Jogador |X| informe a posição LINHA-COLUNA(0-0 ou 1-1)')
    
    #try:
       #str_posicao = int(str_posicao)
    #except ValueError:
        ##
       #raise ValueError('ALGUMA COISA')
    
   
    print(40*'-')
    coluna = int(str_posicao[0])
    linha = int(str_posicao[2])
    matriz[coluna][linha] = '|X|'
    jogo_da_velha()
    print(40*'-')
    str_posicao = input('Jogador |O| informe a posição LINHA-COLUNA(0-0 ou 1-1)')
    
    #try:
       #str_posicao = int(str_posicao)
    #except ValueError:
        ##
       #raise ValueError('ALGUMA COISA')
    #print(40*'-')
    
    coluna = int(str_posicao[0])
    linha = int(str_posicao[2])
    matriz[coluna][linha] = '|O|'
    jogo_da_velha()
    
    
    
    