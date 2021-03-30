x = int(input())
y = int(input())
lista = []

if x > y:
    aux = x
    x = y
    y = aux
if x > 0 and y > 0:
    for z in range(x + 1, y):
        if z % 5 == 2 or z % 5 == 3:
            lista.append(z)

    for num in lista:
        print(num)
