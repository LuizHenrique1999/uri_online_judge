lista = input().split()

b = float(lista[0])
c = float(lista[1])
a = float(lista[2])

lista2 = [a, b, c]

lista2.sort()

b = (lista2[0])
c = (lista2[1])
a = (lista2[2])

if a > 0 and b > 0 and c > 0:
    if a >= b + c:
        print('NAO FORMA TRIANGULO')
        exit()
    if (a ** 2) == ((b ** 2) + (c ** 2)):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > ((b ** 2) + (c ** 2)):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < ((b ** 2) + (c ** 2)):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    if a != b and b == c or b != a and c == a:
        print('TRIANGULO ISOSCELES')

