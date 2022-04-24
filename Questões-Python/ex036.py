valor_casa = float(input())
salario = float(input())
anos = int(input())

pecent = salario * 0.30
parcela = valor_casa / (anos * 12)

if parcela > pecent:
    print("NEGADO")

else:
    print("APROVADO")
