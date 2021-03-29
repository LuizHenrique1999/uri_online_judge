

def isPrimo(valor):


    divisores = []
    
    if valor == 0 or valor == 1:

        return False

    for valores in range(1, valor + 1):
        if valor % valores == 0:
            
            divisores.append(valores)
    
    if len(divisores) > 2:
        return False
    else:
        return True

entrada = int(input())

for x in range(entrada):

    valor = int(input())
    check = isPrimo(valor)

    if check:

        print("%d eh primo" % valor)
    else:

        print("%d nao eh primo" % valor)





