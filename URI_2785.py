wall_size = int(input())
wall = [list(map(int, input().split())) for line in range(wall_size)]
levels_weights = [[sum(wall[row][col:col + row + 1]) for col in range(wall_size - row)]
                  for row in range(wall_size)]
for row in range(1, wall_size):
    for col in range(0, wall_size - row):
        levels_weights[row][col] += min(levels_weights[row - 1][col:col + 2])
print(levels_weights[-1][0])
