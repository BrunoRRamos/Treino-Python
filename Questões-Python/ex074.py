import random


maior = 0
menor = 999999999999

a = (random.randint(0, 10))
b = (random.randint(0, 10))
c = (random.randint(0, 10))
d = (random.randint(0, 10))
e = (random.randint(0, 10))

sec = (a, b, c, d, e)

for x in range(0, len(sec)):
    if sec[x] > maior:
        maior = sec[x]

    if sec[x] < menor:
        menor = sec[x]

a1 = str(a)
b1 = str(b)
c1 = str(c)
d1 = str(d)
e1 = str(e)

tup = a1, b1, c1, d1, e1

print(tup)

print(f'O maior é : {maior}')
print(f'O menor é : {menor}')