n = int(input())
m = 1
print('%d %d %d' % (m, m, m))
print('%d %d %d' % (m, m + 1, m + 1))
for x in range(n - 1):
    m += 1
    aux = m
    aux_2 = aux * m
    print('%d %d %d' % (m, aux * m, aux_2 * m))
    print('%d %d %d' % (m, (aux * m) + 1, (aux_2 * m) + 1))

