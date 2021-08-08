from operator import add


while True:
    try:
        field_size = list(map(int, input().split()))
    except EOFError:
        break

    cb_positions = [list(map(int, input().split())) for row in range(field_size[0])]
    neighbors_sides = [list(map(add, row[1:] + [0], [0] + row[:-1])) for row in cb_positions]
    neighbors_up = [[0 for col in range(field_size[1])]] + cb_positions[:-1]
    neighbors_down = cb_positions[1:] + [[0 for col in range(field_size[1])]]

    for row in range(field_size[0]):
        for col in range(field_size[1]):
            if cb_positions[row][col] > 0:
                print(9, end='')
            else:
                print(neighbors_sides[row][col] + neighbors_up[row][col] + neighbors_down[row][col], end='')
        print()
