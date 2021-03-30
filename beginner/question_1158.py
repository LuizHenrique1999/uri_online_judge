N = int(input())
total = 0
limite = N


while 0 < N:
    count = 0
    
    lista = input().split()
    x = int(lista[0])
    y = int(lista[1])

    if x % 2 == 0:
        aux = x + 1
    else:
        aux = x

    while True:

        if count == y:
            print(total)
            break

        if aux % 2 != 0:
            total += aux
            count += 1
        aux += 1
    total = 0
    N -= 1







