import sys
from math import log2

def count_ones(n):
    if n == 0:
        return 0
    count = 0
    for p in range(int(log2(n)) + 1):
        pow2 = 2 ** p
        rep, rem = divmod(n, pow2)
        blocks_1, block_rem = divmod(rep, 2)
        count += blocks_1 * pow2 + block_rem * (rem + 1)
    return count


if __name__ == '__main__':
    for input_lines in sys.stdin:
        a, b = map(int, input_lines.split())
        print(count_ones(b) - count_ones(a - 1))

#  Os digitos binários de ordem n seguem o seguinte padrão:
#    [0]*2^n + [1]*2^n + [0]*2^n + ...
#
#  Ou seja, se contarmos até um certo número N, temos que passar por N/(2^n) blocos de repetição completos. Chamando de
# B p número de blocos de repetição, podemos dizer que:
#    B_1 = B / 2
# é o número de blocos compostos por 2^n dígitos 1. Então, a quantidade de dígitos 1 em blocos completos é:
#    Ones_b = N / (2^n) / 2 * 2^n
#
#  O que sobra é contar a quantidade de dígitos 1 em blocos não completos. A quantidade de dígitos é simplesmente:
#    d = N % (2^n)
# e os dígitos serão B % 2
