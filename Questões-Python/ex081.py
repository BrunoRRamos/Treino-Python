valores = []

while True:
    a = int(input('Digite umm valor:'))
    valores.append(a)

    x = str(input('Deseja continuar ? S / N').lower())
    if x == 'n':
        break


print(f'Existem {len(valores)} itens na lista !!')
valores.sort(reverse= True)

print(f'A lista de forma decrescente é {valores}')
if 5 in valores:
    print('O valor 5 está na lista !!')
else:
    print('O valor 5 não está na lista !!')