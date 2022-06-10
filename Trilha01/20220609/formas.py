class FormaGeometrica:
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None

    def calcular_area(self):
        return (self.base * self.altura) / 2
        
triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'Preto'
triangulo_a.cor_borda = 'Verde'
triangulo_a.espessura_borda = 3
triangulo_a.base = 100
triangulo_a.altura = 50
print(f'Calculo da área do quadrado {round(triangulo_a.calcular_area())}')

class Quadrilatero(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return self.base * self.altura


quadrado = Quadrilatero()
quadrado.cor_fundo = 'Verde'
quadrado.cor_borda = 'Azul'
quadrado.espessura_borda = 4
quadrado.base = 10
quadrado.altura = 10

print(f'Calculo da área do quadrado {quadrado.calcular_area()}')



























