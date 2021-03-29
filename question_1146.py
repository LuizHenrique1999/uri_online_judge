lista = []
while True:
    x = int(input())

    if x == 0:
        break
    for num in range(1, x + 1):
        lista.append(num)
    res = " ".join([str(n) for n in lista])
    print(res)
    lista.clear()















