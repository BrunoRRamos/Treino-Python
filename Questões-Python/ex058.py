import random

n = random.randint(0, 10)
tentativas = 0

while True:
    m = int(input())

    if n == m:
        print('ACERTOU')
        print('Você tentou {} vezes !'.format(tentativas))
        break

    if n != m:
        tentativas +=1
