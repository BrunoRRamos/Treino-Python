n1 = int(input())
n2 = int(input())
n3 = int(input())

ordem = []

ordem.append(n1)
ordem.append(n2)
ordem.append(n3)

ordem.sort()

print('maior {}, menor {}'.format(ordem[-1], ordem[0]))

