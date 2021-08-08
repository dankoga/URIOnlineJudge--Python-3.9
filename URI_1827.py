while True:
    try:
        matrix_size = int(input())
    except EOFError:
        break

    matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]
    for row in range(matrix_size):
        matrix[row][row] = 2
        matrix[row][matrix_size - row - 1] = 3

    limits_begin = matrix_size // 3
    limits_end = matrix_size - limits_begin
    for row in range(limits_begin, limits_end):
        for col in range(row, limits_end):
            matrix[row][col] = 1
            matrix[col][row] = 1

    center = matrix_size // 2
    matrix[center][center] = 4

    for row in range(matrix_size):
        print(''.join([str(n) for n in matrix[row]]))
    print()
