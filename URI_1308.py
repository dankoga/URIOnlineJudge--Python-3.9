from math import sqrt

cases_qty = int(input())
for c in range(cases_qty):
    warriors_qty = float(input())
    print(int((sqrt(1 + 8.0 * warriors_qty) - 1.0) / 2.0))
