from math import sin, cos, sqrt

PI = 3.14159
G = 9.80665

while True:
    try:
        height = float(input())
    except EOFError:
        break
    target_begin, target_end = map(float, input().split())
    shots_qty = int(input())
    for s in range(shots_qty):
        angle, speed = map(float, input().split())
        angle *= PI / 180.0
        vx = speed * cos(angle)
        vy = speed * sin(angle)
        x = (vy + sqrt(vy * vy + 2 * G * height)) * vx / G
        if target_begin <= x <= target_end:
            print('{:.5f} -> DUCK'.format(x))
        else:
            print('{:.5f} -> NUCK'.format(x))
