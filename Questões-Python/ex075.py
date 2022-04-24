a = int(input())
b = int(input())
c = int(input())
d = int(input())

tup = (a, b, c, d)

print(tup.count(9))

for x in range(0, len(tup)):
    if tup[x] == 3:
        print(x)

for x in range(0, len(tup)):
    if tup[x] % 2 == 0:
        print(tup[x], end=" ")