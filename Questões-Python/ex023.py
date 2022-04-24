num = str(input())
if len(num) > 4:
    print("valor mt alto deve ser ate 9999")
    exit(0)

else:

    if len(num) == 4:
        print('unidades {}'.format(num[3]))
        print('dezena {}'.format(num[2]))
        print('centena {}'.format(num[1]))
        print('milhar {}'.format(num[0]))

    if len(num) == 3:
        print('unidades {}'.format(num[2]))
        print('dezena {}'.format(num[1]))
        print('centena {}'.format(num[0]))

    if len(num) == 2:
        print('unidades {}'.format(num[1]))
        print('dezena {}'.format(num[0]))

    if len(num) == 1:
        print('unidades {}'.format(num[0]))
