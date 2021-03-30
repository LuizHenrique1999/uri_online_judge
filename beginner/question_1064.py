# Número positivos e a média dos positivos
listaPares = []
count = 0
for x in range(1, 7):

    n = float(input())
    if n > 0:
        listaPares.append(n)
        count += 1
media = (sum(listaPares)) / count
print('%d valores positivos' % count)
print('%.1f' % media)
