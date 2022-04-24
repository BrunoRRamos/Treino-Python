valores = []
par = []
impar = []

while True:
    a = int(input('Digite umm valor:'))
    valores.append(a)

    x = str(input('Deseja continuar ? S / N').lower())
    if x == 'n':
        break

for x in range(len(valores)):
    if valores[x] % 2 == 0:
        par.append(valores[x])
    else:
        impar.append(valores[x])

print(f'A lista dos pares é: {par}')
print(f'A lista dos impares é: {impar}')
