while True:
    try:
        grid_size = list(map(int, input().split()))
    except EOFError:
        break
    positions = [[0, 0],
                 [0, 0]]
    for row in range(grid_size[0]):
        input_line = list(map(int, input().split()))
        for col, cell in enumerate(input_line):
            if cell > 0:
                positions[cell - 1][0] = row
                positions[cell - 1][1] = col
    print(abs(positions[0][0] - positions[1][0]) + abs(positions[0][1] - positions[1][1]))
