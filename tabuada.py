while True:
    n = int(input("qual tabuada você quer saber?"))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
    print('FINALIZANDO PROGRAMA. VOLTE SEMPRE!')

