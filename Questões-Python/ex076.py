produtos = ('AWP Asiimov', 387.32, 'M4A4 Howl', 34556.98, 'Ak-47 Neon Revolution', 76.98)

for x in range(0, len(produtos), 2):
    print(f'{produtos[x]} ........................ R$ {produtos[x + 1]}')