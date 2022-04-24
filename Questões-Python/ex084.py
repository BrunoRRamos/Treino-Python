pessoas = list()
mais_p = list()
menos_p = list()
unit = list()
peso_med = 70

#ENTRADA DE DADOS
while True:

    a = str(input('Digite o nome: '))
    b = int(input(('Digite o peso: ')))

    unit.append(a)
    unit.append(b)
    pessoas.append(unit[:])
    unit.clear()

    x = str(input('Deseja continuar ? S / N').lower())
    if x == 'n':
        break
#LISTAS DOS PESADOS E LEVES
for x in range(0, len(pessoas)):
    if pessoas[x][1] > 70:
        mais_p.append(pessoas[x][0])
    else:
        menos_p.append(pessoas[x][0])


print(f'Foram cadastradas {len(pessoas)} !!')
print(f'Os mais pesados são: {mais_p}')
print(f'Os mais leves são: {menos_p}')