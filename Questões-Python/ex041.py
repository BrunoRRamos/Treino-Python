idade = int(input())

if idade <= 9:
    print('Mirim')

elif 9 < idade <= 14:
    print('infantil')

elif 14 < idade <= 19:
    print('Junior')

elif idade == 20:
    print('senior')

elif idade > 20:
    print('master')
