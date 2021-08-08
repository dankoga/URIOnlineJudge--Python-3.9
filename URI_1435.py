matrix_size = int(input())
while matrix_size > 0:
    matrix = [[1 for col in range(matrix_size)] for row in range(matrix_size)]
    for row in range(1, matrix_size // 2 + 1):
        for col in range(row, matrix_size - row):
            matrix[row][col] = row + 1
            matrix[col][row] = row + 1
            matrix[matrix_size - row - 1][col] = row + 1
            matrix[col][matrix_size - row - 1] = row + 1

    for row in range(matrix_size):
        for col in range(matrix_size - 1):
            print('{:3d}'.format(matrix[row][col]), end=' ')
        print('{:3d}'.format(matrix[row][matrix_size - 1]))
    print()
    matrix_size = int(input())
