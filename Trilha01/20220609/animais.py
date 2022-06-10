class Cachorro:
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
            print(f'Agora estou {self.status.title()} zzzZZZZZZZZzzzzzzzZZZ...  U ´ᴥ` U ')
        else:
            print(f'Não posso dormir, pois já estou {self.status.title()} o sono X-X zzZZZzzzzzZZzzzz   U ´ᴥ` U ')
        self.status = 'DORMINDO'
        
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Agora estou acordado! 🐕')
        else:
            print(f'Já estou {self.status.title()}! 🐕')
            
    def correr(self):
        if self.status == 'ACORDADO':
            print(f'Agora estou correndo!')
        else:
            print(f'Não posso correr pois estou {self.status.title()}')
            
    def latir(self):
        if self.status == 'ACORDADO':
            print(f'Agora estou latindo AU AU AU AU!!')
        else:
            print(f'Não posso latir pois estou {self.status.title()}')
            
    def comer(self):
        if self.status == 'ACORDADO':
            print(f'Agora estou comendo!')
        else:
            print(f'Não posso comer pois estou {self.status.title()}')
        
        
        
        
        
        
        
        
        
        
        
        