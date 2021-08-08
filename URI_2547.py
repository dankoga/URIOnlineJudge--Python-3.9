while True:
    try:
        guests_qty, height_min, height_max = map(int, input().split())
    except EOFError:
        break

    guests_allowed = 0
    for guest in range(guests_qty):
        guest_height = int(input())
        if height_min <= guest_height <= height_max:
            guests_allowed += 1
    print(guests_allowed)
