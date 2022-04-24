while True:
    n = int(input('Digite qual número você deseja visualizar a tabuada:'))
    if n < 0:
        print('Finalizando...')
        break

    for x in range(1, 11):
        print(f' {n} x {x} = {n * x}')

    while True:
        resp = str(input('Deseja visualizar outra tabuada ?? [S / N]').upper())

        if resp == "S" or resp == "N":
            break
        else:
            print('Entrada invalida, tente novamente !!')

    if resp == 'N':
        print('Finalizando...')
        break
    elif resp == 'S':
        continue