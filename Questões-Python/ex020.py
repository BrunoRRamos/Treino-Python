import random

alunos = []
ordem = []

for y in range(0, 4):
    x = str(input())
    alunos.append(x)

while True:
    m = random.randint(0, 3)
    if alunos[m] in ordem:
        pass

    else:
        ordem.append(alunos[m])

    if len(ordem) == 4:
        break

for x in range(0, 4):
    print(ordem[x])
