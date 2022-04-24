n1 = float(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

while True:

    print('[1] SOMAR:')
    print('[2] MULTIPLICAR:')
    print('[3] MAIOR:')
    print('[4] NOVOS NUMEROS:')
    print('[5] SAIR:')

    n = int(input())

    if n == 1:
        print('a soma é', n1 + n2)

    if n == 2:
        print('a multiplicação é', n1 * n2)

    if n == 3:
        if n1 > n2:
            print('o maior é', n1)
        else:
            print('o maior é', n2)

    if n == 4:
        n1 = float(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))

    if n == 5:
        break