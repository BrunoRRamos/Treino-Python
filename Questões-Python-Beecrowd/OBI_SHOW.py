files = []
empty_assents = 0
best_file = 0
consec = 0

n_amigos, n_filas, n_assentos = input().split(' ')

n_amigos = int(n_amigos)
n_filas = int(n_filas)
n_assentos = int(n_assentos)

if n_assentos < n_amigos:
    print(-1)
    exit(0)
else:
    for x in range(0, n_filas):
        files.append(input().split(' '))
        
    files.pop(0)
    files.reverse()
    
    for file in range(0, len(files)):
        for assent in range(0, len(files[file])):
            if str(files[file][assent]) == '0' :
                empty_assents += 1
                consec += 1
            else:
                consec = 0
            
        if consec >= n_amigos:
            print(file + 1)
            exit(0)
        else:
            empty_assents = 0
            
print(-1)