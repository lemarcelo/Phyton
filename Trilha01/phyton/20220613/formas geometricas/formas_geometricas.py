from math import pi

class FormaGeometrica:
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
    def metodo_geral(self):
        print('Eu sou uma forma geometrica')
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None
    
    def __str__(self):
        return f'eu sou um Triangulo de base {self.base} e altura {self.altura}'
    
    def calcular_area(self):
        return (self.base*self.altura) / 2
    
    def metodo_geral(self):#Mesmo nome setado em FormaGeometrica
        super().metodo_geral()#Esse comando executa a função criada na mãe
        print('Metodo geral da calsse filha')
    
class Quadrilatero(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return self.base*self.altura

class Circulo(FormaGeometrica):
    raio = None
    
    def calcular_area(self):
        return pi*self.raio**2
    def __str__(self):
        return f'eu sou um Círculo de raio {self.raio}'


