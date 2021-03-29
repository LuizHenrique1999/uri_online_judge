lista = []
while True:
    n = float(input())

    if 0.0 < n < 10.1:
        lista.append(n)
    else:
        print('nota invalida')
    if len(lista) == 2:
        res = (lista[0] + lista[1]) / 2
        print('media = %.2f' % res)
        break

