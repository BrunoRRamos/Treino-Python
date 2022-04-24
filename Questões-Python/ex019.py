import random

alunos = []
for y in range(0, 4):
    x = str(input())
    alunos.append(x)

a = random.randint(0, 3)

print(alunos[a])