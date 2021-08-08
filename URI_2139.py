CUMULATIVE_DAYS = [0,
                   31,
                   60,
                   91,
                   121,
                   152,
                   182,
                   213,
                   244,
                   274,
                   305,
                   335]

while True:
    try:
        month, day = map(int, input().split())
    except EOFError:
        break

    day_of_year = CUMULATIVE_DAYS[month - 1] + day
    if day_of_year < 359:
        print('Faltam {} dias para o natal!'.format(360 - day_of_year))
    elif day_of_year == 359:
        print('E vespera de natal!')
    elif day_of_year == 360:
        print('E natal!')
    else:
        print('Ja passou!')
