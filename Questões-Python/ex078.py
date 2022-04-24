valores = []

maior = 0
chave_maior = 0

menor = 999999999999999999
chave_menor = 0

for x in range(0, 5):
    a = int(input())
    valores.append(a)

for v in range(0, len(valores)):
    if valores[v] > maior:
        maior = valores[v]
        chave_maior = v

    if valores[v] < menor:
        menor = valores[v]
        chave_menor = v

print(f'O maior valor foi {maior} na posição {chave_maior}')
print(f'O menor valor foi {menor} na posição {chave_menor}')