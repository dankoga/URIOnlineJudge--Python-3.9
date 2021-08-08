while True:
    try:
        volume = float(input())
        diameter = float(input())
    except EOFError:
        break

    area = 0.785 * diameter ** 2
    print('ALTURA = {:.2f}'.format(volume / area))
    print('AREA = {:.2f}'.format(area))
