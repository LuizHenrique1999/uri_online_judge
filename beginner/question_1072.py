# inteiros entre 10 e 20

N = int(input())
countIn = 0
countOut = 0
if N < 10000:
    for i in range(1, N + 1):
        X = int(input())
        if X > (-10 ** 7) and X < (10 ** 7):
            if X >= 10 and X <= 20:
                print('caiu no if %d' % i)
                countIn += 1
            else:
                print('caiu no else %d' % i)
                countOut += 1
print('%d in' % countIn)
print('%d out' % countOut)
