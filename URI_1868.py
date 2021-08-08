def rotate(v):
    return [v[1], -v[0]]


def print_matrix(m):
    for line in m:
        print(''.join([str(n) for n in line]).replace('0', 'O').replace('1', 'O').replace('2', 'X'))


while True:
    matrix_size = int(input())
    if matrix_size == 0:
        break
    if matrix_size == 1:
        print('X\n@')
        continue

    matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]
    position = [matrix_size // 2, matrix_size // 2]
    move_dir = [0, 1]
    feel_dir = [1, 0]

    while position != [matrix_size, matrix_size - 1]:
        matrix[position[1]][position[0]] = 2
        print_matrix(matrix)
        print('@')
        matrix[position[1]][position[0]] = 1
        if matrix[position[1] + feel_dir[1]][position[0] + feel_dir[0]] == 0:
            move_dir = rotate(move_dir)
            feel_dir = rotate(feel_dir)
        position = [position[0] + move_dir[0], position[1] + move_dir[1]]
