preco = float(input())
pag = str(input())

if pag == 'dinheiro' or pag == 'cheque':
    print(preco * 0.90)

elif pag == 'cartao':
    tipo = str(input())

    if tipo == 'a vista':
        print(preco * 0.95)

    elif tipo == 'parcelado':
        parcelas = int(input())

        if parcelas == 2:
            print(preco)

        elif parcelas >= 3:
            print(preco * 1.20)
