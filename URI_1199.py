while True:
    number = input()
    if number[0] == '-':
        break
    elif number[0] == '0':
        print(int(number, 16))
    else:
        print('0x' + format(int(number), 'X'))
