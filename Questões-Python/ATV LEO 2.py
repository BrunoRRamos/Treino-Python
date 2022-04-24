desloc, tempo = input().split(" ")

desloc = float(desloc)
tempo = float(tempo)
temp_seg = (tempo * 60) * 60

print("A velocidade média é: {:.2f} m/s".format((desloc / temp_seg)))