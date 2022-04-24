d, km = input().split(" ")

d = int(d)
km = float(km)

print("O valor a pagar é: {:.2f}".format((d * 60) + (km * 0.15)))
