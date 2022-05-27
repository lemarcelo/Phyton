for item in range(0, 11):
    if item%2 == 0:
        print(f'O número {item} é par, expoente {item**2}')
    elif item%2 != 0:
        print(f'O número {item} é impar, expoente {item**2}')
    else:
        print('\nTerminei o for')
print('\nTerminei o for')