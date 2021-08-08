people_per_floor = [int(input()), int(input()), int(input())]

time = [people_per_floor[1] + 2 * people_per_floor[2],
        people_per_floor[0] + people_per_floor[2],
        2 * people_per_floor[0] + people_per_floor[1],]
print(2 * min(time))
