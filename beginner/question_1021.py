n = float(input())

cem = n / 100
cinq = n % 100 / 50
vinte = n % 100 % 50 / 20
dez = n % 100 % 50 % 20 / 10
cinco = n % 100 % 50 % 20 % 10 / 5
dois = n % 100 % 50 % 20 % 10 % 5 / 2
um = n % 100 % 50 % 20 % 10 % 5 % 2 / 1
cinqcents = (n + 0.001) % 100 % 50 % 20 % 10 % 5 % 2 % 1 / 0.50
vinte_cinco_centavos = (n + 0.001) % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 / 0.25
dez_centavos = (n + 0.001) % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 / 0.10
cinco_centavos = (n + 0.001) % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 / 0.05
um_centavo = (n + 0.001) % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % cem)
print('%d nota(s) de R$ 50.00' % cinq)
print('%d nota(s) de R$ 20.00' % vinte)
print('%d nota(s) de R$ 10.00' % dez)
print('%d nota(s) de R$ 5.00' % cinco)
print('%d nota(s) de R$ 2.00' % dois)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % um)
print('%d moeda(s) de R$ 0.50' % cinqcents)
print('%d moeda(s) de R$ 0.25' % vinte_cinco_centavos)
print('%d moeda(s) de R$ 0.10' % dez_centavos)
print('%d moeda(s) de R$ 0.05' % cinco_centavos)
print('%d moeda(s) de R$ 0.01' % um_centavo)







