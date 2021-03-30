
N = int(input())

for z in range(N):
    lista = [int(num)for num in input().split()]
    X = min(lista)
    Y = max(lista)
    somaImpar = 0

    for num in range(X + 1, Y):
        if num % 2 == 1:
            somaImpar += num
    print(somaImpar)



