#  Questão 1020 da Uri Judge
diasTotais = int(input())
ano = diasTotais / 365  # 400 / 365 = 1 ano
meses = ((diasTotais % 365) / 30)  # 35 / 30 = 1 dias
dias = ((diasTotais % 365) % 30)  # 400 / 365 = 35 % 30 = 5 dias


print('%d ano(s)' % ano)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)














