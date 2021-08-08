while True:
    try:
        number = input()
    except EOFError:
        break
    if number == '0':
        print('vai ter copa!')
    else:
        print('vai ter duas!')
