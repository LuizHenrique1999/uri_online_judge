salario = float(input())

if salario > 0 and salario <= 400:

    bonus = (salario * 0.15)
    salario = salario + (salario * 0.15)
    adicionado = 15
    print('Novo salario: %.2f' % salario)
    print('Reajuste ganho: %.2f' % bonus)
    print('Em percentual: %d %%' % adicionado)

elif salario >= 400.01 and salario <= 800.00:

    bonus = (salario * 0.12)
    salario = salario + (salario * 0.12)
    adicionado = 12
    print('Novo salario: %.2f' % salario)
    print('Reajuste ganho: %.2f' % bonus)
    print('Em percentual: %d %%' % adicionado)

elif salario >= 800.01 and salario <= 1200.00:

    bonus = (salario * 0.10)
    salario = salario + (salario * 0.10)
    adicionado = 10
    print('Novo salario: %.2f' % salario)
    print('Reajuste ganho: %.2f' % bonus)
    print('Em percentual: %d %%' % adicionado)

elif salario >= 1200.01 and salario <= 2000.00:

    bonus = (salario * 0.07)
    salario = salario + (salario * 0.07)
    adicionado = 7
    print('Novo salario: %.2f' % salario)
    print('Reajuste ganho: %.2f' % bonus)
    print('Em percentual: %d %%' % adicionado)

elif salario > 2000.00:

    bonus = (salario * 0.04)
    salario = salario + (salario * 0.04)
    adicionado = 4
    print('Novo salario: %.2f' % salario)
    print('Reajuste ganho: %.2f' % bonus)
    print('Em percentual: %d %%' % adicionado)





