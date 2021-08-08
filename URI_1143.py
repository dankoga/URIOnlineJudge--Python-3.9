lines_qty = int(input())
for line in range(lines_qty):
    number = line + 1
    number2 = number ** 2
    number3 = number2 * number
    print('{} {} {}'.format(number, number2, number3))
