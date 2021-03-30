def novo_calculo():
    while True:
        print('novo calculo (1-sim 2-nao)')
        novo_calc = float(input())
        if novo_calc == 1:
            repete_operacao()
        elif novo_calc == 2:
            exit()
        elif novo_calc != 1 and novo_calc != 2:
            continue


def repete_operacao():
    lista_repete = []
    while True:
        n = float(input())

        if n >= 0 and n < 10.01:
            lista_repete.append(n)
        else:
            print('nota invalida')
        if len(lista_repete) == 2:
            res = (lista_repete[0] + lista_repete[1]) / 2
            print('media = %.2f' % res)
            break


repete_operacao()
novo_calculo()











