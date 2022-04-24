valor = int(input('Valor a ser sacado: R$'))

por_50 = valor // 50
rest_50 = valor % 50

por_20 = rest_50 // 20
rest_20 = rest_50 % 20

por_10 = rest_20 // 10
rest_10 = rest_20 % 10


print(f' {por_50} notas de 50, {por_20} notas de 20, {por_10} notas de 10, {rest_10} notas de 1')