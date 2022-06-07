#Função para receber inteiro
def entrar_inteiro():
    #Inicializa a variavel a favor do looping(while)
    solicitar_inteiro = True
    #Enquanto a variável de controle(solicitar_Inteiro) for True, execute...
    while True:
        #Tente converter o valor do input em int
        try:
            solicitar_inteiro = False
            #Return tira o usuário do while
            return int(input('Informe um número inteiro'))
        except:
            print(f"{20*'-'} Você deve digitar um número inteiro! {20*'-'}")
numero = entrar_inteiro()
print(f'O dobro de {numero} é {2*numero}')