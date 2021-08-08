
while True:
    try:
        matrix_size = int(input())
    except Exception:
        break

    matrix = [[3 for col in range(matrix_size)] for row in range(matrix_size)]
    for row in range(matrix_size):
        matrix[row][row] = 1
        matrix[row][matrix_size - row - 1] = 2

    for row in range(matrix_size):
        for col in range(matrix_size - 1):
            print('{}'.format(matrix[row][col]), end='')
        print('{}'.format(matrix[row][matrix_size - 1]))
