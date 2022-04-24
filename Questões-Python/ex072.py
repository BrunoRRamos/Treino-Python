ordem = 'um', 'dois', 'três', 'quatro', 'cinco'

while True:
    n = int(input('Digite um número de 1 á 5: '))
    if 1 <= n <= 5:
        break

print(ordem[n-1])
