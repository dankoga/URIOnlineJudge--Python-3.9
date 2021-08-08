ships_qty = int(input())
ships_position = [list(map(int, input().split())) for s in range(ships_qty)]

distances2_matrix = [[0 for col in range(ships_qty)] for row in range(ships_qty)]
for s1 in range(ships_qty):
    for s2 in range(s1 + 1, ships_qty):
        distance_vector = [ships_position[s1][0] - ships_position[s2][0],
                           ships_position[s1][1] - ships_position[s2][1],
                           ships_position[s1][2] - ships_position[s2][2]]
        distance2 = distance_vector[0] ** 2 + distance_vector[1] ** 2 + distance_vector[2] ** 2
        distances2_matrix[s1][s2] = distance2
        distances2_matrix[s2][s1] = distance2

for s1 in range(ships_qty):
    distance2_next = min(distances2_matrix[s1][:s1] + distances2_matrix[s1][(s1 + 1):])
    if distance2_next <= 400:
        print('A')
    elif distance2_next < 2500:
        print('M')
    else:
        print('B')
