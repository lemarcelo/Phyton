from time import sleep
#Modelagem - P O O 
#Caracteristicas = atributos
# Ações = métodos
class Caneta:
    #atributos
    cor = None
    modelo = None
    qtd_tinta = 10
    
    def __init__(self, cor = None, modelo = None, qtd_tinta = 0):
        #Criação das variáveis
        self.cor = cor
        self.modelo = modelo
        
    #métodos da minha classe
    def riscar(self, ):
        #Self usar o escopo para dentro da classe
        if self.qtd_tinta:
            print('opuɐɔsı̣ɹ noʇsǝ nƎ')
            self.qtd_tinta -=1
        else:
            print('Estou sem tinta, não posso riscar')

caneta_a = Caneta(cor = 'Azul', modelo = 'Caneta para quadro branco')

print(f'Cor da caneta {caneta_a.cor}')
print(f'Modelo da caneta {caneta_a.modelo}')
print(f'Quantidade de tinta inicial {caneta_a.qtd_tinta}')

"""

for i in range(0,11):
    caneta_a.riscar()
    caneta_b.riscar()
    sleep(1)
"""