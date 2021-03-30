j = 7
for i in range(1, 10, 2):
    print('I=%d J=%d' % (i, j))
    j -= 1
    print('I=%d J=%d' % (i, j))
    j -= 1
    print('I=%d J=%d' % (i, j))
    j += 4