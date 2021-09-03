from math import lcm


def check_connections(b):
    p = [0] * len(b)
    for i in range(len(p)):
        p[i] += 1
        next_hole = b[i] - 1
        while next_hole != i:
            p[i] += 1
            next_hole = b[next_hole] - 1
    return p


if __name__ == '__main__':
    digletts_qty = int(input())
    holes_connections = list(map(int, input().split()))
    digletts_periods = check_connections(holes_connections)
    print(lcm(*digletts_periods))
