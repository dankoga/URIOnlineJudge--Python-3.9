from math import log10

def print_row(input_row, index, size, field):
    format_str = '{:>' + str(field) + 'd}'
    for i in range(index, index + size - 1):
        print(format_str.format(input_row[i]), end=' ')
    print(format_str.format(input_row[index + size - 1]))


matrix_size = int(input())
while matrix_size > 0:
    row_list = [2 ** number for number in range(0, 2 * matrix_size - 1)]
    field_size = int(log10(row_list[-1])) + 1
    for row in range(matrix_size):
        print_row(row_list, row, matrix_size, field_size)
    print()
    matrix_size = int(input())
