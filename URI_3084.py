while True:
    try:
        angle_H, angle_M = map(int, input().split())
    except EOFError:
        break
    print("{:02d}:{:02d}". format(angle_H // 30, angle_M // 6))
