x = int(input())
lista = [0, 1, 1]

for n in range(x):

    soma = lista[-1] + lista[-2]
    lista.append(soma)


valores = lista[:x]

print(' '.join(str(x) for x in valores))



    
    


    



    
    