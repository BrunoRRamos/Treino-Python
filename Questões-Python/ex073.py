times = 'Natus Vincere', 'Luminosity', 'Faze Clan', 'Sk Gaming', 'Ninjas in Pijamas', 'Immortals', 'Big', 'Gambit', 'Astralis', 'Virtus Pro', 'Titan '

print(f'Os 5 primeiros colocados são: {times[0:6]}')
print(f'Os 4 últimos do Ranking são: {times[-1:-5:-1]}')
print(f'A lista de times em ordem alfabetica é: {sorted(times)}')
print(f'O time da Sk Gaming está na posição: {times.index("Sk Gaming") + 1}')