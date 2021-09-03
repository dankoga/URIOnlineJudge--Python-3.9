import sys

for input_line in sys.stdin:
    distance, velocity_fugitive, velocity_guard = map(int, input_line.split())
    if 144 * (velocity_guard ** 2) >= (144 + distance ** 2) * (velocity_fugitive ** 2):
        print('S')
    else:
        print('N')
