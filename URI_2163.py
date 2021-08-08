def search_neighbor(field, row, col):
    return (field[row + 1][col] == 7 and
            field[row - 1][col] == 7 and
            field[row][col + 1] == 7 and
            field[row][col - 1] == 7 and
            field[row + 1][col + 1] == 7 and
            field[row + 1][col - 1] == 7 and
            field[row - 1][col + 1] == 7 and
            field[row - 1][col - 1] == 7)


rows_qty, cols_qty = map(int, input().split())
search_field = [list(map(int, input().split())) for row in range(rows_qty)]

lightsaber_found = False
lightsaber_position = [0, 0]
row = 1
while row < rows_qty - 1 and not lightsaber_found:
    occurrence_cols = [col for col, value in enumerate(search_field[row][1:-1], start=1) if value == 42]
    for col in occurrence_cols:
        if search_neighbor(search_field, row, col):
            lightsaber_position = [row + 1, col + 1]
            lightsaber_found = True
            break
    row += 1

print(*lightsaber_position)
