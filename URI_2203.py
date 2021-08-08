from math import dist


while True:
    try:
        input_values = list(map(float, input().split()))
    except EOFError:
        break

    my_position = input_values[0:2]
    enemy_position = input_values[2:4]
    enemy_speed = input_values[4]
    attack_radius = input_values[5:]

    enemy_distance = dist(my_position, enemy_position) + 1.5 * enemy_speed
    if enemy_distance <= attack_radius[0] + attack_radius[1]:
        print('Y')
    else:
        print('N')
