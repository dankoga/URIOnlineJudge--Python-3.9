tests_qty = int(input())
for t in range(tests_qty):
    N, p, n = map(float, input().split())
    q = 1.0 - p

    P_0 = (q ** (n - 1)) * p
    QN = q ** N
    print('{:.4f}'.format(P_0/(1.0 - QN)))


#  Probabilidade do jogador n ganhar na primeira rodada:
#     P(n; N, 0) = (q ** (n - 1)) * p
#
#  Probabilidade de uma rodada inteira sem vencedores:
#     Q(N) = q ** N
#
#  Probabilidade do jogador n ganhar na g-ésima rodadas:
#    P(n; N; g) = Q(N) ** g * P(n; N, 0)
#
#  Probabilidade do jogador n ganhar em qualquer rodada:
#    P(n, N) = P(n; N, 0) + P(n; N, 1) + P(n; N, 2) + ...
#    P(n, N) = P(n; N, 0) + Q(N) * P(n; N, 0) + Q(N) ** 2 *P(n; N, 0)
#    P(n, N) = P(n; N, 0) * (Q(N) + Q(N) ** 2 + Q(N) ** 3 +...)
#
#  Como Q(N) < 1.0:
#    P(n, N) = P(n; N, 0) / (1 - Q(N))
