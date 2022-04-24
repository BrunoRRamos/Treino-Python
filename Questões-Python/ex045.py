import random

jog = ['pedra', 'papel', 'tesoura']

while True:
    jogada = str(input())
    pc = jog[random.randint(0, 2)]

    if jogada == 'pedra' and pc == 'tesoura':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc ganhou')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'pedra' and pc == 'papel':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc perdeu')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'pedra' and pc == 'pedra':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('empate')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'papel' and pc == 'pedra':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc ganhou')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'papel' and pc == 'tesoura':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc perdeu')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'papel' and pc == 'papel':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('empate')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'tesoura' and pc == 'papel':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc ganhou')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'tesoura' and pc == 'pedra':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('vc perdeu')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue

    elif jogada == 'tesoura' and pc == 'tesoura':

        print('sua jogada: {}'.format(jogada))
        print('jogada do pc: {}'.format(pc))
        print('empate')

        cont = str(input('Continuar ?: S / N'))

        if cont == 'N':
            break
        else:
            continue