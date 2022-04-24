produto_barato = ''
menor_preco = 999999999999999
total = 0
qts_mais_1000 = 0

while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o valor do produto:'))

    if preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    if preco > 1000:
        qts_mais_1000 += 1

    total += preco

    while True:
        resp = str(input('Deseja continuar ? S/N ').lower())

        if resp == 's' or resp == 'n':
            break

    if resp == 'n':
        print('CALCULANDO...')
        break

print(f'Total gasto foi de R${total}')
print(f'Houveram {qts_mais_1000} produto(os) custando mais que R$1000')
print(f'O produro mais barato foi {produto_barato} custando R${menor_preco}')