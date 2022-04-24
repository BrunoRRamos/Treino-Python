count = 0
soma = 0

while True:
    n = int(input())

    if n == 999:
        print(count, soma, "\n")
        exit(0)
    else:
        count += 1
        soma += n