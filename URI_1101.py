while True:
    number_M, number_N = map(int, input().split())
    if number_M <= 0 or number_N <= 0:
        break
    if number_M > number_N:
        buffer = number_M
        number_M = number_N
        number_N = buffer

    for number in range(number_M, number_N + 1):
        print(number, end=' ')
    print('Sum={}'.format((number_N - number_M + 1) * (number_M + number_N) // 2))
