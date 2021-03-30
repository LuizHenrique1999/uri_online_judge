n = int(input())
fat = n
count = fat
for valor in range(fat - 1):
    fat -= 1
    n = n * fat
print(n)


# 1 loop
# resultado = 4 * 3
# resultado = 12

# 2 loop
# 12 = 12 * 2 = 24

# 3 loop
# 24 = 24 * 1 = 24