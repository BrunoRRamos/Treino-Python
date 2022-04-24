n1 = float(input())
n2 = float(input())

md = (n1 + n2) / 2

if md < 5:
    print('REPROVADO')

elif 5 <= md <= 6.9:
    print('RECUPERAÇÃO')

elif md >= 7:
    print('APROVADO')