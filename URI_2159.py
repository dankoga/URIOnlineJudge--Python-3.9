from math import log

number = float(input())
constant = number/log(number)
print('{:.1f} {:.1f}'.format(constant, 1.25506 * constant))
