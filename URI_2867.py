from math import log10


tests_qty = int(input())
for t in range(tests_qty):
    base, exponent = map(float, input().split())
    print(int(exponent * log10(base)) + 1)
