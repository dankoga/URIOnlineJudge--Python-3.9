fraction_sum = 1.0
for n in range(1, 20):
    fraction_sum += (2*n + 1)/(2 ** n)
print('{:.2f}'.format(fraction_sum))
