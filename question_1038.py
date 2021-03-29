lista = input().split()
codigo = int(lista[0])
qtd = int(lista[1])

if codigo < 0 or qtd <= 0:
    exit()
if codigo == 1:
    valor = float(qtd * 4)
elif codigo == 2:
    valor = float(qtd * 4.50)
elif codigo == 3:
    valor = float(qtd * 5)
elif codigo == 4:
    valor = float(qtd * 2)
elif codigo == 5:
    valor = float(qtd * 1.50)
print('Total: R$ %.2f' % valor)















