while True:
    number_a, number_b = map(int, input().split())
    if number_a == number_b == 0:
        break

    number_str = str(number_a + number_b)
    print(''.join([digit for digit in number_str if digit != '0']))
