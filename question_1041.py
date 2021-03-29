lista = input().split()

x = float(lista[0])
y = float(lista[1])

if x == 0 and y == 0:
    print('Origem')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif y < 0 and x > 0:
    print('Q4')
elif y < 0 and x < 0:
    print('Q3')
elif x == 0 and y > 0 or y < 0:
    print('Eixo Y')
elif y == 0 and x > 0 or x < 0:
    print('Eixo X')















