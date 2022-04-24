from datetime import date

maior = 0
menor = 0

for x in range(0, 7):
    ano = int(input())
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1

print(maior)
print(menor)
