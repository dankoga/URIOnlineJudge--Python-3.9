input_size = int(input())
for input_case in range(input_size):
    number = int(input())
    if number == 0:
        print('NULL')
        continue

    if number % 2:
        print('ODD', end = ' ')
    else:
        print('EVEN', end = ' ')

    if number > 0:
        print('POSITIVE')
    else:
        print('NEGATIVE')