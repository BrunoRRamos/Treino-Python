h = 0
mais_18 = 0
m_mais_20 = 0

while True:

    sexo = str(input('H/M').lower())
    idade = int(input('Idade'))

    if sexo == 'h':
        h += 1

    if sexo == 'm':
        if idade < 20:
            m_mais_20 += 1

    if idade >= 18:
        mais_18 += 1

    resp = str(input('DESEJA CADASTRAR OUTRO ? S/N').lower())
    if resp == 'n':
        print('CARREGANDO DADOS CADASTRADOS...')
        break

print(mais_18)
print(h)
print(mais_18)