class Dog:
    nome = None
    raca = None
    tamanho = None
    pelo = None
    status = 'ACORDADO'

    def escrever_quem_sou(self):
        print(f'Olá, eu sou {self.nome} da raça {self.raca} e estou {self.status.title()}')
        
    def dormir(self):
        if self.status == 'ACORDADO':
            self.status = 'DORMINDO'
            print('Agora estou dormindo zzzZZZZZZZZzzzzzzzZZZ...  U ´ᴥ` U ')
        else:
            print('Já estou iniciando o sono X-X zzZZZzzzzzZZzzzz   U ´ᴥ` U ')
            # TODO: write code...
        self.status = 'DORMINDO'
        
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Agora estou acordado! 🐕')
        else:
            print('Já estou acordado! 🐕')
            
    def comer(self):
        if self.status != 'DORMINDO' or self.status != 'COMENDO':
            self.status = 'COMENDO'
            print(f'Agora estou {self.status}!')
        else:
            print(f'Não posso comer, pois eu estava {self.status.title()}!!')
            
    def correr(self):
        if self.status != 'DORMINDO' or self.status != 'COMENDO' or self.status != 'CORRENDO':
            self.status = 'CORRENDO'
            print(f'Agora estou {self.status}!')
        else:
            print(f'Não posso correr, pois eu estava {self.status}')
            
    def latir(self):
        if self.status != 'COMENDO' or self.status != 'DORMINDO' or self.status != 'LATINDO':
            self.status = 'LATINDO'
            print('Agora estou Latindo AU! AU! AU! AU! AU!')
        else:
            print(f'Não posso latir porque agora estou {self.status}')
        
        
        
        
        
        
        
        
        
        
        
        
        