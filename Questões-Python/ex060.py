n = int(input())
ordem = []
controle = 1

fatorial = n

while True:
    if controle == n:
        break
    else:
        ordem.append(n - controle)
        controle += 1

for x in range(0, len(ordem)):
    fatorial *= ordem[x]

print(fatorial)