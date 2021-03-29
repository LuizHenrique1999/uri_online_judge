
while True:

    x = int(input())
    count = 0
    total = 0
    
    if x == 0:
        break
    
    if x % 2 == 0:
        aux = x
    else:
        aux = x + 1
        
    while True:

        if count == 5:
            print(total)
            break

        if aux % 2 == 0:
            total += aux
            count += 1
        aux += 1






     
