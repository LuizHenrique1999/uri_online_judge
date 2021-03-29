while True:
    lista = input().split()
    X = int((lista[0]))
    Y = int((lista[1]))

    if X == Y:
        break
    elif X > Y:
        print("Decrescente")
    else:
        print("Crescente")

