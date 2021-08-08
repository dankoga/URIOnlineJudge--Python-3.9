from operator import sub


SPELLS = {'fire':  [200, 20, 30, 50],
          'water': [300, 10, 25, 40],
          'earth': [400, 25, 55, 70],
          'air':   [100, 18, 38, 60]}


def clamp_value(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def spell_hit(spell_position, spell_radius, target_position, target_size):
    nearest_target_point = [clamp_value(spell_position[i], target_position[i], target_position[i] + target_size[i])
                            for i in [0, 1]]
    distance = list(map(sub, nearest_target_point, spell_position))
    return distance[0] * distance[0] + distance[1] * distance[1] <= spell_radius * spell_radius


cases_qty = int(input())
for case in range(cases_qty):
    input_line = list(map(int, input().split()))
    target_size = input_line[:2]
    target_position = input_line[2:]
    input_line = list(input().split())
    spell_name = input_line[0]
    spell_level = int(input_line[1])
    spell_position = [int(input_line[2]), int(input_line[3])]

    if spell_hit(spell_position, SPELLS[spell_name][spell_level], target_position, target_size):
        print(SPELLS[spell_name][0])
    else:
        print(0)
