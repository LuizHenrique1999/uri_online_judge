
def isPerfect():

    valor = int(input())
    lista_divisores = []
    count = 1

    while count < valor:

        if valor % count == 0:
            lista_divisores.append(count)
        
        count += 1
    
    if sum(lista_divisores) == valor:
        check = True
    else:
        check = False
    
    return check, valor

entradas = int(input())

for x in range(entradas):

    check, valor = isPerfect()

    if check:
        print("%d eh perfeito" % valor)
    else:
        print("%d nao eh perfeito" % valor)


    








