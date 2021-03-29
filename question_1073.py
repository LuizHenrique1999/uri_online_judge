# Quadrado de cada numero de 1 ate N
import math
N = int(input())
for x in range(1, N + 1):
    if x % 2 == 0:
        print("%d^%d = %d" % (x, 2, x ** 2))







