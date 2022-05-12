a, b = input().split(" ")
c, d = input().split(" ")

a = float(a)
b = float(b)
c = float(c)
d = float(d)

val = ((c - a) ** 2 + (d - b) ** 2) ** (1/2)    

print('{:.4f}'.format(val))