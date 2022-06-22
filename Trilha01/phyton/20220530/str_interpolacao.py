nome = 'Marcelo'
idade = 27

print('Olá ' + nome + 'Seja Bem-vindo!')

str_1 = 'Olá ' + nome + ' Seja Bem-vindo!'
str_2 = 'Olá %s seja bem-vindo!'% nome
str_3 = 'Olá %s seja bem-vindo! Você tem %d anos' % (nome, idade)
str_4 = 'Olá {nome} seja bem vindo! Você tem {idade} anos.'.format(nome = nome, idade = idade)
print(str_1)
print(str_2)
print(str_3)
print(str_4)
print(f"Olá {nome} seja bem-vindo!{20*'-'} Você tem {idade} anos.  {20*'-'}")
