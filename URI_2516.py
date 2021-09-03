import sys

if __name__ == '__main__':
    for data in sys.stdin:
        distance, speed_a, speed_b = map(float, data.split())
        if speed_b >= speed_a:
            print('impossivel')
        else:
            print('{:.2f}'.format(distance / (speed_a - speed_b)))
