# Pares,ímpares, positivos e negativos entre os 5

countPares = 0
countImpares = 0
countPositivos = 0
countNegativos = 0
for x in range(1, 6):
    n = int(input())
    if n % 2 == 0:
        countPares += 1
    else:
        countImpares += 1
    if n > 0:
        countPositivos += 1
    elif n < 0 and n != 0:
        countNegativos += 1
print('%d valor(es) par(es)' % countPares)
print('%d valor(es) impar(es)' % countImpares)
print('%d valor(es) positivo(s)' % countPositivos)
print('%d valor(es) negativo(s)' % countNegativos)
