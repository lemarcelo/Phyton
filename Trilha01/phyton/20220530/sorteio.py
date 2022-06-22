from random import randint
nivel = input('Informe o nível do jogo, [F] para facil e [D] para difícil')

if(nivel.upper() == 'F'):
    qtd_chances = 6
elif (nivel.upper() == 'D'):
    qtd_chances = 4
else:
    print(f'Ops! você digitou {nivel}, esta opção é inválida')
    exit()
    
nr_sorteado = randint(0, 10)

for chance in range(1, qtd_chances):
    nr_digitado = int(input('Informe um número de 0 a 10'))
    if nr_sorteado == nr_digitado:
        print('Parabéns você foi sorteado!!!!')
        exit()
    else:
        if chance == qtd_chances:
            mensagem = 'Reinicie o jogo'
            exit()
        else:
            mensagem = 'Tente novamente'
            print(f'Errrrrrrrrou! {mensagem}')
print(f'Número sorteado era {nr_sorteado}')

#print(f'Nr escolhido {nr_usuario} Nr sorteado {nr_sorteado}')  