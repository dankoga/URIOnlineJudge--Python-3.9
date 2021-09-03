import sys
from math import sqrt

PI = 3.1415926535897

for input_line in sys.stdin:
    a, b, c = map(float, input_line.split())
    abc = a * b * c
    s = (a + b + c) / 2
    sm = (s - a) * (s - b) * (s - c)
    ssm = s * sm

    a1 = PI * abc * abc / ssm / 16.0
    a2 = sqrt(ssm)
    a3 = PI * sm / s

    print('{:.4f} {:.4f} {:.4f}'.format(a1 - a2, a2 - a3, a3))
