while True:
    number_a, number_b = input().split()
    if number_a == number_b == '0':
        break

    number_b = ('{:0>' + str(len(number_a)) + '}').format(number_b)
    number_a = ('{:0>' + str(len(number_b)) + '}').format(number_a)

    carry = 0
    total_carries = 0
    for i in reversed(range(len(number_a))):
        carry = int(int(number_a[i]) + int(number_b[i]) + carry > 9)
        total_carries += carry
    if total_carries == 0:
        print('No carry operation.')
    elif total_carries == 1:
        print('1 carry operation.')
    else:
        print('{} carry operations.'.format(total_carries))
