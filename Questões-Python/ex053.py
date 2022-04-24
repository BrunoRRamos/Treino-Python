n = str(input())
vazio = []
separado = n.split()
sem_espacos = ''.join(separado)

if sem_espacos == sem_espacos[::-1]:
    print(True)

else:
    print(False)
