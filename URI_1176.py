from math import sqrt, pow

SQRT5 = sqrt(5.0)
PHI = (1 + SQRT5) / 2.0

input_size = int(input())
for input_line in range(input_size):
    fibonacci_n = float(input())
    print('Fib({:.0f}) = {:.0f}'.format(fibonacci_n, round(pow(PHI, fibonacci_n) / SQRT5)))
