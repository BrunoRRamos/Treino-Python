termo_um = int(input())
r = int(input())
c = 0

while c != 10:

    if c == 0:
        print(termo_um)
        c += 1

    else:
        print(termo_um + r)
        termo_um += r
        c += 1
