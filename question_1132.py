x = int(input())
y = int(input())
lista = []

if x > y:
    aux = x
    x = y
    y = aux
for x in range(x, y + 1):
    if x % 13 != 0:
        lista.append(x)
print(sum(lista))

