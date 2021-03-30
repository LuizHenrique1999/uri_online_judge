count = 0
total = 0
while True:

    idade = int(input())

    if idade < 0:
        break

    count += 1
    total += idade
    
resultado = (total / count)
print('%.2f' % resultado)
    
