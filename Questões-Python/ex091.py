from random import  randint
sec = []
sec2 = []
l2 = []
dados = dict()

jogador1 = str(input('Nome do Jogador: '))
dados['jogador1'] = jogador1
dado1 = randint(1, 6)
dados['dado1'] = dado1

jogador2 = str(input('Nome do Jogador: '))
dados['jogador2'] = jogador2
dado2 = randint(1, 6)
dados['dado2'] = dado2

jogador3 = str(input('Nome do Jogador: '))
dados['jogador3'] = jogador3
dado3 = randint(1, 6)
dados['dado3'] = dado3

jogador4 = str(input('Nome do Jogador: '))
dados['jogador4'] = jogador4
dado4 = randint(1, 6)
dados['dado4'] = dado4

sec.append(dados['dado1'])
sec.append(dados['dado2'])
sec.append(dados['dado3'])
sec.append(dados['dado4'])

l2.append(sec[:])
sec.sort()

print(sec)