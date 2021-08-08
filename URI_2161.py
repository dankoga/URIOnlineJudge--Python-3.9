iterations_qty = int(input())
fractional_term = 0.0
for iteration in range(iterations_qty):
    fractional_term = 1.0 / (6.0 + fractional_term)
print('{:.10f}'.format(3.0 + fractional_term))
