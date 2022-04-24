valores = [[],[]]

for x in range(0, 7):
    a = int(input('Digite um valor: '))
    if a % 2 == 0:
        valores[0].append(a)
    else:
        valores[1].append(a)

valores[0].sort()
valores[1].sort()
print(f'Os valores pares são: {valores[0]}')
print(f'Os valores impares são: {valores[1]}')