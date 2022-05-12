valor = float(input())

por_100 = valor // 100
rest_100 = valor % 100

por_50 = rest_100 // 50
rest_50 = rest_100 % 50

por_20 = rest_50 // 20
rest_20 = rest_50 % 20

por_10 = rest_20 // 10
rest_10 = rest_20 % 10

por_5 = rest_10 // 5
rest_5 = rest_10 % 5

por_2 = rest_5 // 2
rest_2 = rest_5 % 2

# Moedas

por_1 = rest_2 // 1
rest_1 = rest_2 % 1

por_05 = rest_1 // 0.5
rest_05 = rest_1 % 0.5

por_025 = rest_05 // 0.25
rest_025 = rest_05 % 0.25

por_010 = rest_025 // 0.1
rest_010 = rest_025 % 0.1

por_005 = rest_010 // 0.05
rest_005 = rest_010 % 0.05

por_001 = rest_005 // 0.01

print(valor)
print(f'{int(por_100)} nota(s) de R$ 100,00')
print(f'{int(por_50)} nota(s) de R$ 50,00')
print(f'{int(por_20)} nota(s) de R$ 20,00')
print(f'{int(por_10)} nota(s) de R$ 10,00')
print(f'{int(por_5)} nota(s) de R$ 5,00')
print(f'{int(por_2)} nota(s) de R$ 2,00')
print('MOEDAS:')
print(f'{int(por_1)} moeda(s) de R$ 1,00')
print(f'{int(por_05)} moeda(s) de R$ 0,50')
print(f'{int(por_025)} moeda(s) de R$ 0,25')
print(f'{int(por_010)} moeda(s) de R$ 0,10')
print(f'{int(por_005)} moeda(s) de R$ 0,05')
print(f'{int(por_001)} moeda(s) de R$ 0,01')