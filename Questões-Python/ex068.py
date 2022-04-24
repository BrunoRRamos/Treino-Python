import random


vitorias = 0

while True:
    pc = random.randint(0, 100)
    n = int(input('Digite um número:'))
    p_i = str(input('Escolha P / I').lower())

    num = pc + n

    if p_i == 'p':
        if num % 2 == 0:
            vitorias += 1
            print('VOCÊ VENCEU !!!!!')

        else:
            print(f'VOCÊ PERDEU :(, com {vitorias}  consecutivas')
            break

    if p_i == 'i':
        if num % 2 != 0:
            print('VOCÊ VENCEU !!!!!')

        else:
            print(f'VOCÊ PERDEU :(, com {vitorias}  consecutivas')
            break