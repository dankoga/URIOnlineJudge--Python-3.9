from math import sqrt

SQRT5 = sqrt(5)
PHI = (1.0 + SQRT5) / 2.0
PSI = (1.0 - SQRT5) / 2.0

number = float(input())
print('{:.1f}'.format((pow(PHI, number) - pow(PSI, number)) / SQRT5))
