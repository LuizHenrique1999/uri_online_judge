lista = input().split()

a = int(lista[0])
b = int(lista[1])

if b % a == 0:

    print('Sao Multiplos')

elif a % b == 0:

    print('Sao Multiplos')
else:

    print('Nao sao Multiplos')