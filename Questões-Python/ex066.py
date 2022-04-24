count = 0
soma = 0

while True:
    n = int(input())
    if n == 999:
        break
    else:
        count += 1
        soma += n

print(f'Quantidade de números foi {count} e a soma deles foi {soma}')
