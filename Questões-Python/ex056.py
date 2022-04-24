h_velho = 0
nome_maisvelho = ""
med_id = 0
m_21 = 0

for x in range(0, 4):
    sexo = str(input().lower())
    idade = int(input())
    nome = str(input())

    med_id += idade

    if sexo == "homem" and idade > h_velho:
        h_velho = idade
        nome_maisvelho = nome

    if sexo == "mulher" and idade < 20:
        m_21 += 1

print('media {:.2f}'.format(med_id / 4))

if h_velho == 0:
    print("nao tem homem")
else:
    print(nome_maisvelho, h_velho)

print(m_21)