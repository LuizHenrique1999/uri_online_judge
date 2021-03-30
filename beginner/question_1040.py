lista = input().split()

n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
n4 = float(lista[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if media > 7:

    mediaFinal = media
    print('Media: %.1f' % media)
    print('Aluno aprovado.')

elif media < 5:

    mediaFinal = media
    print('Media: %.1f' % media)
    print('Aluno reprovado.')

if 5 <= media <= 6.9:
    print('Media: %.1f' % media)
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame: %.1f' % notaExame)
    mediaExame = (notaExame + media) / 2
    mediaFinal = mediaExame

    if mediaExame >= 5:

        print('Aluno aprovado.')
        print('Media final: %.1f' % mediaFinal)

    else:

        print('Aluno reprovado.')
        print('Media final: %.1f' % mediaFinal)
