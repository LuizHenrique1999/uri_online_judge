# Média ponderada
N = int(input())

for x in range(1, N + 1):
    lista = input().split()
    a = float(lista[0])
    b = float(lista[1])
    c = float(lista[2])
    media = ((a * 2) + (b * 3) + (c * 5)) / (2 + 3 + 5)
    print('%.1f' % media)










