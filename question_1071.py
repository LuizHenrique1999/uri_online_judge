# Soma dos valores ímpares entre x e y.

X = int(input())
Y = int(input())
somaImpares = 0

if X < Y:
    for i in range(X + 1, Y + 1):
        if i % 2 != 0:
            somaImpares += i
elif X > Y:
    for n in range(X - 1, Y, -1):
        if n % 2 != 0:
            somaImpares += n
print(somaImpares)

