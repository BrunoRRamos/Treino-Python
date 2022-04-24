matriz = [[], [], []]
m = 0

for x in range(0, 3):
    for k in range(0, 3):
        e = int(input())
        matriz[m].append(e)
    m += 1

for x in matriz:
    print(x)