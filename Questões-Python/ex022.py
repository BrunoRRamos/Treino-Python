nome = str(input())

print(nome.upper())
print(nome.lower())

separado = nome.split()
sem_espacos = ''.join(separado)

print(len(sem_espacos))

print(len(separado[0]))
