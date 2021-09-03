import sys

for input_line in sys.stdin:
    velocity, time = map(int, input_line.split())
    print(2 * velocity * time)
