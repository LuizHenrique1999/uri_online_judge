T = int(input())

for i in range(T):

    count = 0
    lista = input().split()
    PA = int(lista[0])
    PB = int(lista[1])
    G1 = float(lista[2])
    G2 = float(lista[3])

    while PA <= PB:
        
        PA = PA + int((PA*G1)/100)
        PB = PB + int((PB*G2)/100)
        
        count += 1
        if count > 100:
            print("Mais de 1 seculo.")
            break

    
    if count <= 100:
        print("%d anos." % count)
    
    