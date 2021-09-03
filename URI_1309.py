while True:
    try:
        dollars = input()[::-1]
    except EOFError:
        break
    cents = input()

    dollars = ','.join(dollars[i:i + 3] for i in range(0, len(dollars), 3))
    print('${}.{:>02}'.format(dollars[::-1], cents))
