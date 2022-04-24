ano = int(input())
u = ano // 1000 % 10

if ano == 1900:
    print(False)
    exit(0)

elif u == 0 or u == 2 or u == 4 or u == 6 or u == 8:
    print(True)
