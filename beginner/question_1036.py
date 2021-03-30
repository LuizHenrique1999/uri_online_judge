import math
lista = input().split()

A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

x = (B ** 2) - (4 * A * C)

if x >= 0 and (2 * A) != 0:
    x = math.sqrt(x)
    R1 = (-B + x) / (2 * A)
    R2 = (-B - x) / (2 * A)
    print('R1 = %.5f' % R1)
    print('R2 = %.5f' % R2)
else:
    print("Impossivel calcular")












