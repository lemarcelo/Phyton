#Função para receber inteiro
def entrar_inteiro():
    #Inicializa a variavel a favor do looping(while)
    solicitar_inteiro = True
    #Enquanto a variável de controle(solicitar_Inteiro) for True, execute...
    while solicitar_inteiro:
        #Tente converter o valor do input em int
        try:
            inteiro = int(input('Informe um número inteiro'))
            #Passando pela conversão desabilita o looping alterando a variável de controle(solicitar_inteiro) para false
            solicitar_inteiro = False
            return inteiro
        except:
            #pass somente ignora e segue
            #pass
            #código não necessário só para tornar explicito que a variável de controle permanece a favor do looping
            solicitar_inteiro = True
            #Aviso de erro
            print(f"{20*'-'} Você deve digitar um número inteiro! {20*'-'}")
entrar_inteiro()