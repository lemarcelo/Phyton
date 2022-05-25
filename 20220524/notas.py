print(20*'-','Notas', 20*'-')
trim_1 = float(input('Informe a nota do 1º trimestre'))
trim_2 = float(input('Informe a nota do 2º trimestre'))
trim_3 = float(input('Informe a nota do 3º trimestre'))

media = (trim_1 + trim_2 + trim_3) / 3

if media >= 6:
    print(45*'-')
    print('Aluno aprovado!')
    print('Média: ', round(media, 2))
else:
    print(40*'-')
    print('Aluno reprovado!')
    print('Média: ', round(media, 2))
    
    
print(20*'-','Fim', 20*'-')
