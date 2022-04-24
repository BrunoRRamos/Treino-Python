n = int(input())

for x in range(2, n):
    if n % x == 0:
        print(False)
        exit(0)

print(True)