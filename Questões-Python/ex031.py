d = int(input())
taxa_200 = 0.50
taxa_maior = 0.45

if d <= 200:
    print('taxa {}, preço {:.2f}'.format(taxa_200, d * taxa_200))

else:
    print('taxa {}, preço {:.2f}'.format(taxa_maior, d * taxa_maior))
