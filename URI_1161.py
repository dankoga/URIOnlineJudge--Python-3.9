import sys
from math import factorial

for input_line in sys.stdin:
    number_a, number_b = map(int, input_line.split())
    print(factorial(number_a) + factorial(number_b))
