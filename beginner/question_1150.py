x = int(input())
count = 1
aux = x
while True:
    y = int(input())
    if y > x:
        while x <= y:
            aux += 1
            x += aux
            count += 1
        break
print(count)




    
    
       
       











