import math

mq = float(input('Insira o valor em metros quadrados: '))

l = mq / 3

latas = l / 18

if latas == float(latas):
    latas = math.ceil(latas)

print(f'Serão utilizadas {latas} latas de tinta !!')