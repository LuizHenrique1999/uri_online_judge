count_alcool = 0
count_gasolina = 0
count_diesel = 0

while True:
    combustivel = int(input())

    if combustivel == 1:
        count_alcool += 1
    elif combustivel == 2:
        count_gasolina += 1
    elif combustivel == 3:
        count_diesel += 1
    elif combustivel == 4:
        break
    else:
        continue
print('MUITO OBRIGADO')
print('Alcool: %d' % count_alcool)
print('Gasolina: %d' % count_gasolina)
print('Diesel: %d' % count_diesel)
















