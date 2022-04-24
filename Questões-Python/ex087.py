matriz = [[], [], []]
m = 0
tot = 0
tot_3 = 0

for x in range(0, 3):
    for k in range(0, 3):
        e = int(input())
        matriz[m].append(e)
    m += 1

#SOMA DOS VALORES DA MATRIZ
for x in range(0, len(matriz)):
    tot += sum(matriz[x])

#SOMA DA 3 COLUNA DA MATRIZ
for x in range(0, len(matriz)):
    tot_3 += matriz[x][2]


print(tot)
print(tot_3)
print(max(matriz[1]))
