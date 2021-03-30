
s = 1
a = 3
b = 2
aux = 0
for x in range(1,19):
    b += aux
    s = s + a/b
    aux = b
    a += 2

print("%.2f" % s)

    
