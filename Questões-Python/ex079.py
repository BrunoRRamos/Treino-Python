valores = []

while True:
    a = int(input('Digite umm valor:'))
    if a not in valores:
        valores.append(a)

    x = str(input('Deseja continuar ? S / N').lower())
    if x == 'n':
        break

valores.sort()
print(f'A lista em ordem crescente é:', end=" ")
for x in valores:
    print(x, end=" ")