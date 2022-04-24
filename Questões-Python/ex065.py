count = 0
soma = 0
maior = 0
menor = 9999999

while True:
    n = int(input())

    count += 1
    soma += n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    pross = str(input("Continuar ? S/N").upper())

    if pross == "N":
        print((soma / count), maior, menor)