import re
import math


def number_to_poly(s):
    return [int(digit) for digit in reversed(s)]


def poly_sum(u, v):
    if len(u) > len(v):
        return [u[i] + v[i] for i in range(len(v))] + u[len(v):]
    else:
        return [u[i] + v[i] for i in range(len(u))] + v[len(u):]


def poly_sub(u, v):
    if len(u) > len(v):
        return [u[i] - v[i] for i in range(len(v))] + u[len(v):]
    else:
        return [u[i] - v[i] for i in range(len(u))] + [-b for b in v[len(u):]]


def poly_mul(u, v):
    result = [0] * (len(u) + len(v) - 1)
    for i, a in enumerate(u):
        for j, b in enumerate(v):
            result[i + j] += a * b
    return result


def evaluate_expression(line):
    scanner = re.Scanner([(r"\*|\+", lambda x, y: y),
                          (r"[0-9]+", lambda x, y: number_to_poly(y))])
    tokens, _ = scanner.scan(line)
    poly_stack = [tokens[0]]
    for i in range(1, len(tokens), 2):
        if tokens[i] == '+':
            poly_stack.append(tokens[i+1])
        else:
            poly_stack[-1] = poly_mul(tokens[i+1], poly_stack[-1])
    result = [0]
    for p in poly_stack:
        result = poly_sum(result, p)
    return result


def find_base(p, b):
    begin = 0
    while begin < len(p) and p[begin] == 0:
        begin += 1
    base = []
    p0 = abs(p[begin])
    for n in range(1, int(math.sqrt(p0)) + 1):
        if p0 % n == 0:
            if sum([d * n ** i for i, d in enumerate(p[begin:])]) == 0:
                base.append(n)
            m = p0 // n
            if m != n and sum([d * m ** i for i, d in enumerate(p[begin:])]) == 0:
                base.append(m)
    return [n for n in sorted(base) if n >= b]


while True:
    input_line = input()
    if input_line == '=':
        break
    base_min = max([int(c) for c in input_line if c.isnumeric()]) + 1
    expression_l, expression_r = input_line.split('=')
    poly_l = evaluate_expression(expression_l)
    poly_r = evaluate_expression(expression_r)
    poly = poly_sub(poly_r, poly_l)
    print(poly)
    if all([p == 0 for p in poly]):
        print('{}+'.format(max(2, base_min)))
    else:
        bases = find_base(poly, base_min)
        if len(bases) == 0:
            print('*')
        else:
            print(' '.join([str(b) for b in bases]))


#  Um número em base b pode ser convertido para seu valor decimal usando a fórmula:
#    n_b = d_0 * b^0 + d_1 * b^1 + d_2 * b^2 + ...
#
# onde d_n é o n-ésimo dígito na base b. Por exemplo:
#    213_5 = 3 * 5^0 + 1 * 5^1 + 2 * 5^2 = 58_10
#
#  O problema de se descobrir a base, então, se resume à encontrar as raízes inteiras de um polinômio:
#    p(b) = d0 + d1 * b + d2 * b^2 +...
#
#  Para fazer isso, primeiro temos que lembrar que uma raiz inteira de p(b) sempre é um divisor de d0.
# Assim, listamos os divisores de d0 e procuramos as raízes por tentativa e erro.
#
#  Se d0 for 0, basta assumir 0 como uma raiz trivial e calcular as raízes de p(b)/b.
