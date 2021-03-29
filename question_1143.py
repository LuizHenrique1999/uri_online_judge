n = int(input())
m = 1
print('%d %d %d' % (m, m, m))
for x in range(n - 1):
    m += 1
    aux = m
    aux_2 = aux * m
    print('%d %d %d' % (m, aux * m, aux_2 * m))


















