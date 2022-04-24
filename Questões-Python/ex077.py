palavras = ('cu', 'anao', 'borboleta', 'jaboticaba', 'uva', 'peixe')

vogais = ('a', 'e', 'i', 'o', 'u')

for x in range(0, len(palavras)):
    for k in range(0, len(palavras[x])):
        if palavras[x][k] in vogais:
            print(palavras[x][k], end=' ')

    print()