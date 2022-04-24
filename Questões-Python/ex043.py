peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

print('{:.2f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')

elif 18.5 <= imc < 25:
    print('PESO IDEAL')

elif 25 <= imc < 30:
    print('SOBREPESO')

elif 30 <= imc < 40:
    print('OBESIDADE')

elif imc > 40:
    print('OBESIDADE MORBIDA')