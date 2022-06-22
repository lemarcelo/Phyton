print(40*'-')
ls1 = [1, 8, 4, 20, 3]
ls2 = ['Inter', 'Grêmio', 'Juventide']

ls2.append('Caxias')
print(f'Quantidade de itens da lista 1\n {len(ls1)}')
print(f'Menor valor da lista 1\n {min(ls1)}')
print(f'Maior valor da lista 1\n {max(ls1)}')
print(f'Lista 1 em ordem com Sort\n {ls1.Sort()}')
print(f'Lista 2 em ordem reversa com sorted\n {sorted(ls2, reverse = True)}')
print(f'Trecho da lista 1\n {ls1[0:3]}')
print(40*'-')