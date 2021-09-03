if __name__ == '__main__':
    while True:
        bowls_qty = int(input())
        if bowls_qty == 0:
            break
        marbles = list(map(int, input().split()))
        print(sum([2 ** (i - 1) * m for i, m in enumerate(marbles, start=1)]))


#  A estratégia ótima é esvaziar os potes do último para o primeiro.
#  O chamando o número de bolas no i-ésimo pode te de m_i, usando essa estratégia o número de movimentos para n potes
# será:
#    c = m_n + (m_{n-1} + m_n) + (m_{n-1} + m_{n-2} + 2 * m_n) + ... (m_0 + m_1 + 2 * m_2 + ... + 2^(n-1) * m_n)
#
#  Em outras palavras:
#    c = M_0 * m_0 + M_1 * m1 + ... + M_n * m_n
#
# onde:
#    M_i = 1 + sum(2^k), k = 0..(i-1)
#
#  Usando a fórmula para a soma de progressões geométricas:
#    M_i = 1 + (1 - 2^(i-1)) / (-1)
#    M_i = 2^(i-1)
