positives_qty = 0
positives_total = 0.0
for inputs in range(6):
    number = float(input())
    if number >= 0:
        positives_qty += 1
        positives_total += number
print('{} valores positivos'.format(positives_qty))
print('{:.1f}'.format(positives_total/positives_qty))