sec = []

for x in range(0, 5):
    peso = float(input())
    sec.append(peso)

sec.sort()

print(sec[-1])
print(sec[0])
