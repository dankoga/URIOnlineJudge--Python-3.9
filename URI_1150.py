from math import  sqrt, floor
# an = X + (n - 1)
# Sn = n * (X + an)/2 > Z
# n * (X + X + n - 1) > 2*Z
# n^2 + (2*X - 1)*n - 2*Z > 0

x = float(input())
z = float(input())
while x >= z:
    z = float(input())

delta = sqrt((2.0 * x - 1.0) ** 2  + 8.0 * z)
print('{:.0f}'.format(floor((delta - (2.0 * x - 1.0))/2)+ 1.0))
