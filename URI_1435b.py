matrix_size = int(input())
while matrix_size > 0:
    for row in range(matrix_size):
        for col in range(matrix_size - 1):
            distance = [1 + row, 1 + col, matrix_size - row, matrix_size - col]
            print('{:3d}'.format(min(distance)), end=' ')
        print('{:3d}'.format(1))
    print()
    matrix_size = int(input())
