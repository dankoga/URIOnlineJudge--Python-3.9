def print_row(input_row, index, size):
    for i in range(size - index, 2 * size - index - 1):
        print('{:3d}'.format(input_row[i]), end=' ')
    print('{:3d}'.format(input_row[2 * size - index - 1]))


matrix_size = int(input())
while matrix_size > 0:
    row_list = list(range(matrix_size, 1, -1)) + list(range(1, matrix_size + 1))
    for row in range(1, matrix_size + 1):
        print_row(row_list, row, matrix_size)
    print()
    matrix_size = int(input())
