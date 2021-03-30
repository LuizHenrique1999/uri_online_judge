qtd = int(input())
for i in range(1, qtd + 1):
    lista = input().split()
    x = int(lista[0])
    y = int(lista[1])

    if y == 0:
        print('divisao impossivel')
    else:
        res = float(x / y)
        print(res)





