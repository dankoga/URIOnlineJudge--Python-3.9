if __name__ == '__main__':
    for instance in range(int(input())):
        n = int(input())
        print(1 + (n * (n+1)) // 2)

#  As regras:
#    (1). Nenhum par de linhas paralelas
#    (2). Nenhum ponto de intersecção com mais de uma linha.
#
#    n = 1: área dividida em 2, necessariamente - 1 nova área divididida
#    n = 2: área dividida em 4, necessariamente (regra 1) - 1 intersecção: 2 áreas divididas
#    n = 3: área dividida em 7, necessariamente (regra 2) - 2 intersecções: 3 áreas divididas
#    n = 4: área dividida em 11, necessariamente (regra 2) - 3 intersecções:4 áreas divididas
#  Ou seja, começamos com uma área e, a cada nova linha n, ganhamos n novas áreas, portanto:
#     A(n) = 1 + 1 + 2 + 3 + ... n
#     A(n) = 1 + n * (n + 1) / 2
