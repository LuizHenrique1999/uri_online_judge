lista = input().split()
n1 = int(lista[0])
n2 = int(lista[1])
n3 = int(lista[2])

if n3 < n2:
    aux = n2
    n2 = n3
    n3 = aux
if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux
if n3 < n2:
    aux = n2
    n2 = n3
    n3 = aux
print(n1)
print(n2)
print(n3)
print('')
print(lista[0])
print(lista[1])
print(lista[2])




















