import random
games = []
temp = list()

jogos = int(input('Quantos jogos deseja gerar: '))

for x in range(0, jogos):
    for k in range(0, 6):
        a = random.randint(1, 60)

        if a in temp:
            a = random.randint(1, 60)
            if a not in temp:
                temp.append(a)
        else:
            temp.append(a)

    games.append(temp[:])
    temp.clear()

for x in games:
    print(x)