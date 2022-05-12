id_dias = int(input())

anos = id_dias // 365
rest_anos = id_dias % 365

meses = rest_anos // 30
rest_meses = rest_anos % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{rest_meses} dia(s)')