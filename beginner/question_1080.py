# Maior valor e sua posicao

lista = []

for x in range(1, 101):
    n = int(input())
    lista.append(n)
maior = max(lista)
pos = lista.index(maior)
print(maior)
print(pos+1)


