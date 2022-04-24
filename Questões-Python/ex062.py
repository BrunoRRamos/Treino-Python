termo_um = int(input())
r = int(input())
c = 0
termos = 10
count = 0

while True:

    while c != termos:

        if c == 0:
            print(termo_um)
            c += 1

        else:
            print(termo_um + r)
            termo_um += r
            c += 1

    count += 1
    if count >= 1:
        k = str(input('Deseja fazer com mais termos ? S / N').upper())
        if k == 'S':
            termos = int(input('Digite'))
        else:
            exit(0)