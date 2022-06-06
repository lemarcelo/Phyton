def falador1(qtd, palavra):
    frase = (qtd*palavra)
    print(frase)

def falador(qtd, palavra):
    for cont in range(1, qtd+1):
        print(palavra)

def tela_inicio():
    print('                     ***********************                   ')
    print(65*'-')
    print(f"{22*'-'}Bem vindo ao Programa{20*'-'}")
    print(65*'-')
    
def exponencial(nr_1, nr_2):
    return nr_1 ** nr_2

def somar(nro_1, nro_2):
    return nro_1 + nro_2
    
resultado1 = somar(nro_1 = 8, nro_2 = 10)

resultado2 = somar(nro_1 = 1000, nro_2 = 123)

resultado3 = somar(1000, 123)
"""
resultado4 = somar(, 123)
"""

