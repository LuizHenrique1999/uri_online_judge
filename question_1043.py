lista = input().split()

a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

modulo = abs(b - c)

if modulo < a and modulo < b and modulo < c and a < b + c and b < a + c and c < a + b:
    p = a + b + c
    print('Perimetro = %.1f' % p)
else:
    area = ((a + b) * c) / 2
    print('Area = %.1f' % area)
