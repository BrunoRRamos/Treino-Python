n = int(input('Insira o numero:'))

m = 1
for x in range(0, 10):
    print('{} x {} = {}'.format(n, m, n * m))
    m += 1
