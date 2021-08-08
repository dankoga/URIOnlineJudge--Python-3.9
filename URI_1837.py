dividend, divisor = map(int, input().split())
quotient, remainder = divmod(dividend, divisor)
if remainder < 0:
    quotient += 1
    remainder -= divisor
print('{} {}'.format(quotient, remainder))
