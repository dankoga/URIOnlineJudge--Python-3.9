size_y, size_x = map(int, input().split())
while size_y * size_x != 0:
    drawing = [input() for y in range(size_y)]
    scale_y, scale_x = map(int, input().split())
    drawing_scaled = [scale_y // size_y * (''.join([scale_x // size_x * char for char in line]) + '\n') for line in drawing]
    print(''.join([line for line in drawing_scaled]))
    size_y, size_x = map(int, input().split())
