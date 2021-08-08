while True:
    try:
        number_str = input()
    except EOFError:
        break
    number_str = number_str.replace(' ', '').replace(',', '').replace('o', '0').replace('O', '0').replace('l', '1')
    if not number_str.isnumeric() or int(number_str) >  2147483647:
        print('error')
    else:
        print(int(number_str))
