salario = float(input())

if salario >= 0 and salario <= 2000:

    print('Isento')

elif salario > 2000 and salario <= 3000:

    salario -= 2000
    ir = salario * 0.08
    print('R$ %.2f' % ir)

elif salario > 3000 and salario <= 4500:

    salario -= 3000
    ir = 1000 * 0.08
    ir = ir + (salario * 0.18)
    print('R$ %.2f' % ir)

elif salario > 4500:

    salario -= 4500
    ir = 1000 * 0.08
    ir = ir + (1500 * 0.18)
    ir = ir + (salario * 0.28)
    print('R$ %.2f' % ir)


















