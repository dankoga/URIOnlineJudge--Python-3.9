from math import sqrt, floor

input_list = list(map(float, input(). split()))
while input_list[0] != 0.0:
    house_size1, house_size2, occupancy_max = input_list[0], input_list[1], input_list[2]
    print('{:.0f}'.format(floor(sqrt(house_size1 * house_size2 * 100.0 / occupancy_max))))
    input_list = list(map(float, input(). split()))