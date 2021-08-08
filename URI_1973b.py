star_number = int(input())
star_sheep = list(map(int, input().split()))

sheep_total = sum(star_sheep)
brother_pos = 0
sheep_lonely = 0
while brother_pos < star_number:
    if star_sheep[brother_pos] % 2 == 0:
        break
    else:
        if star_sheep[brother_pos] == 1:
            sheep_lonely += 1
        brother_pos += 1

if brother_pos == star_number:
    print('{} {}'.format(brother_pos, sheep_total - star_number))
else:
    print('{} {}'.format(brother_pos + 1, sheep_total - 2 * brother_pos - 1 + sheep_lonely))
