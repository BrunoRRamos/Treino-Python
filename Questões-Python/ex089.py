alunos = list()
alum = list()

while True:
    print(30*'=-=')

    a = str(input('Digite o nome do aluno:'))
    alum.append(a)

    print(30 * '=-=')

    m = float(input('Nota 1: ').lower())
    alum.append(m)

    print(30 * '=-=')

    k = float(input('Nota 2: ').lower())
    alum.append(k)

    print(30 * '=-=')

    x = str(input('Deseja continuar ? S / N').lower())

    print(30 * '=-=')

    alunos.append(alum[:])
    alum.clear()

    if x == 'n':
        break

for x in range(0, len(alunos)):
    print(f'{x + 1}- A média de {alunos[x][0]} foi de: {(alunos[x][1] + alunos[x][2]) / 2}')

print(30*'=-=')

while True:
    perg = str(input('Deseja saber a nota de algum aluno ? S/N').lower())

    print(30 * '=-=')

    if perg == 's':
        perg2 = int(input('Qual aluno deseja ver ?'))
        print(30 * '=-=')

        print(f'As notas de {alunos[perg2 - 1][0]} são {alunos[perg2 - 1][1]} e {alunos[perg2 - 1][2]}')

        print(30 * '=-=')

    else:
        break
