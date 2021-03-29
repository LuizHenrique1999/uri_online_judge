inter = []
gremio = []
count_grenais = 0
count_inter = 0
count_gremio = 0
empate = 0


def contabilidade():
    while True:

        lista_gols = [int(n) for n in input().split()]
        inter.append(lista_gols[0])
        gremio.append(lista_gols[1])
        inter_soma = int((inter[-1]))
        gremio_soma = int((gremio[-1]))

        if inter_soma > gremio_soma:
            global count_inter
            count_inter += 1
        elif gremio_soma > inter_soma:
            global count_gremio
            count_gremio += 1
        elif gremio_soma == inter_soma:
            global empate
            empate += 1

        global count_grenais
        count_grenais += 1
        break


def escolha():

    while True:

        print('Novo grenal (1-sim 2-nao)')
        escolha = int(input())
        if escolha == 1:
            contabilidade()
        elif escolha == 2:

            print('%d grenais' % count_grenais)
            print('Inter:%d' % count_inter)
            print('Gremio:%d' % count_gremio)
            print('Empates:%d' % empate)

            if count_inter > count_gremio:
                print('Inter venceu mais')
                break
            elif count_gremio > count_inter:
                print('Gremio venceu mais')
                break
            elif count_gremio == count_inter:
                print('Nao houve vencedor')
                break
            elif escolha != 1 and escolha != 2:
                continue


contabilidade()
escolha()





