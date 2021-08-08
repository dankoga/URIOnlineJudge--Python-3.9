distance = int(input())
while distance > 0:
    position = 2
    button_press = 0
    for section in range(distance):
        obstacle = list(map(int, (input().split())))
        if obstacle[position - 1]:
            free_lane = 6 - obstacle[0] - 2 * obstacle[1] - 3 * obstacle[2]
            button_press += abs(position - free_lane)
            position = free_lane
    print(button_press)
    distance = int(input())
