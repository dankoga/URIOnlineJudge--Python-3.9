while True:
    try:
        departure_H, departure_M = map(int, input().split(':'))
    except EOFError:
        break
    delay = 60 * departure_H + departure_M - 420
    if delay > 0:
        print('Atraso maximo: {}'.format(delay))
    else:
        print('Atraso maximo: 0')
