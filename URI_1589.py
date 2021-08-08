input_size = int(input())
for input_line in range(input_size):
    radius_1, radius_2 = map(int, input().split())
    print('{}'.format(radius_1 + radius_2))