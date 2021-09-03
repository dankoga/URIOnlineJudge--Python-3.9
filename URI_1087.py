if __name__ == '__main__':
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == y1 == x2 == y2 == 0:
            break

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if dx == dy == 0:
            print(0)
        elif dx == dy or dx == 0 or dy == 0:
            print(1)
        else:
            print(2)
