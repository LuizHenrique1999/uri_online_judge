# Cobaias
listaCobaia = ['R', 'S', 'C']
listaCoelhos = []
listaRatos = []
listaSapos = []
n = int(input())

for x in range(1, n + 1):
    animal = input()
    distri = animal.split()
    novaDistri = int(distri[0])
    if distri[1] == 'R':
        listaRatos.append(novaDistri)
    elif distri[1] == 'S':
        listaSapos.append(novaDistri)
    elif distri[1] == 'C':
        listaCoelhos.append(novaDistri)
coelhos = sum(listaCoelhos)
ratos = sum(listaRatos)
sapos = sum(listaSapos)
total = coelhos + ratos + sapos
print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % coelhos)
print('Total de ratos: %d' % ratos)
print('Total de sapos: %d' % sapos)
print('Percentual de coelhos: %.2f %%' % ((coelhos * 100)/total))
print('Percentual de ratos: %.2f %%' % ((ratos * 100)/total))
print('Percentual de sapos: %.2f %%' % ((sapos * 100)/total))

















