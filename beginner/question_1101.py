while True:
    lista = [int(num) for num in input().split()]
    menor = min(lista)
    maior = max(lista)
    soma = 0
    if lista[0] == 0 or lista[1] == 0 or lista[0] < 0 or lista[1] < 0:
        break
    for x in range(menor, maior + 1):
        print('%d' % menor, end=' ')
        soma += menor
        menor += 1
    print('Sum=%d' % soma, end=' ')
    print('\r')









