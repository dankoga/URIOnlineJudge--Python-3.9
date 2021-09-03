while True:
    n, rate = map(float, input().split())
    if n == 0.0:
        break
    prize = rate / 200.0 * (n ** 2 - 2) * (n ** 2 - 3)
    print('{:.02f}'.format(prize))


#  Se a loteria fosse "linear" o número de vencedores seria igual ao número de combinações de 4 números dentre N^2:
#    Winners(N) = (N^2)! / (4! * (N^2 - 4!))
#
#  Porém, existe a complicação de que os 4 números devem estar em posições específicas, formando quadrados na cartela. O
# número de quadrados (diagonais e paralelos) em uma rede quadrada de N x N pontos é dado pela fórmula:
#     S(N) = N^2 * (N^2 - 1) / 12
# ref: https://www.quora.com/What-are-the-number-of-squares-in-a-square-formed-by-10%C3%9710-dot-square
#
# Então, o número de vencedores será:
#    Winners_square(N) = Winners(N) / S(N)
#
#  Massageando a fórmula usando o Wolfram, cheguei na forma polinomial:
#    1/2 * (N^2 - 2) * (N^2 - 3)
