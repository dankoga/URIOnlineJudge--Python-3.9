def int_ceil(a, b):
    return (a + b - 1) // b


case_number = 1
while True:
    streets_qty, numbers_qty = map(int, input().split())
    if streets_qty == numbers_qty == 0:
        break

    letters_needed = int_ceil(streets_qty - numbers_qty, numbers_qty)
    print('Case {}:'.format(case_number), end=' ')
    if letters_needed <= 26:
        print(letters_needed)
    else:
        print('impossible')
    case_number += 1
