DIGITS_32 = ['0', '1', '2', '3', '4', '5', '6', '7',
             '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

if __name__ == '__main__':
    while True:
        number_10 = int(input())
        if number_10 == 0:
            print(0)
            break

        number_32 = []
        while number_10 > 0:
            number_10, digit = divmod(number_10, 32)
            number_32.append(DIGITS_32[digit])
        print(''.join(number_32[::-1]))
