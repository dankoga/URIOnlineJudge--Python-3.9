star_number = int(input())
star_sheep = list(map(int, input().split()))
star_visited = [0 for star in range(star_number)]

brother_pos = 0
while (0 <= brother_pos < star_number):
    if star_sheep[brother_pos] > 0:
        star_visited[brother_pos] = 1
        star_sheep[brother_pos] -= 1
        if star_sheep[brother_pos] % 2 == 0:
            brother_pos += 1
        else:
            brother_pos -= 1
    else:
        brother_pos -= 1
print(star_sheep)
print('{} {}'.format(sum(star_visited), sum(star_sheep)))
