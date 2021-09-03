from math import lcm

if __name__ == '__main__':
    while True:
        tiles_qty, a, b = map(int, input().split())
        if tiles_qty == a == b == 0:
            break
        print(tiles_qty // a + tiles_qty // b -  tiles_qty // lcm(a, b))
