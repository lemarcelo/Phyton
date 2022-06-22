#Separando os atributos do arquivo formas_geometricas, onde ficam as classes
from formas_geometricas import Triangulo, Quadrilatero, Circulo

formas = []


triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'vermelho'
triangulo_a.cor_borda = 'preto'
triangulo_a.espessura_borda = 3
triangulo_a.base = 100
triangulo_a.altura = 150
formas.append(triangulo_a)

quadrado = Quadrilatero()
quadrado.cor_fundo = 'transparente'
quadrado.cor_borda = 'preto'
quadrado.espessura_borda = 2
quadrado.base = 8
quadrado.altura = 16
formas.append(quadrado)

bolinha = Circulo()
bolinha.cor_borda = 'azul'
bolinha.cor_fundo = 'branca'
bolinha.espessura_borda = 3
bolinha.raio = 10
formas.append(bolinha)

for forma in formas:
    print(forma, 'Area:',forma.calcular_area())

"""
print(quadrado) #-> exibe o objeto na tela, com o endereço de memória junto
print(triangulo_a) #-> exibe um texto que foi definido em na função def __str__ da classe Triangulo()
print(bolinha)
"""

