idade = int(input())

if idade < 18:
    print('falta {} anos'.format(abs(idade - 18)))

elif idade == 18:
    print('esta na hora')

elif idade > 18:
    print('esta atrasado {} anos'.format(abs(idade - 18)))
