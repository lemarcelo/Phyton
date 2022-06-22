from time import sleep
#Modelagem - P O O 
#Caracteristicas = atributos
# Ações = métodos
class Caneta:
    #atributos
    cor = None
    modelo = None
    qtd_tinta = 10
    
    #métodos da minha classe
    def riscar(self, ):
        #Self usar o escopo para dentro da classe
        if self.qtd_tinta:
            print('opuɐɔsı̣ɹ noʇsǝ nƎ')
            self.qtd_tinta -=1
        else:
            print('Estou sem tinta, não posso riscar')

caneta_a = Caneta()
caneta_a.cor = 'Azul'
caneta_a.modelo = 'Caneta para quadro branco'
print(caneta_a.cor)
print(caneta_a.modelo)
print(f'Quantidade de tinta inicial{caneta_a.qtd_tinta}')

caneta_b = Caneta()
caneta_b.cor = 'Preta'
caneta_b.modelo = 'Caneta para quadro branco'
print(caneta_b.cor)
print(caneta_b.modelo)
print(f'Quantidade de tinta inicial{caneta_b.qtd_tinta}')

for i in range(0,11):
    caneta_a.riscar()
    caneta_b.riscar()
    sleep(1)

