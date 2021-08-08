while True:
    try:
        input()
    except EOFError:
        break
    slug_speeds = list(map(int, input().split()))
    slug_speed_max = max(slug_speeds)
    if slug_speed_max < 10:
        print(1)
    elif slug_speed_max < 20:
        print(2)
    else:
        print(3)
