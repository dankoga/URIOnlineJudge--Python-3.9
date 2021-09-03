from math import sqrt, lcm


def divisors(n):
    d = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return sorted(d)


if __name__ == '__main__':
    while True:
        balls_qty, target = map(int, input().split())
        if balls_qty == target == 0:
            break
        balls = list(map(int, input().split()))

        if any([target % b != 0 for b in balls]):
            print('impossivel')
            continue

        balls_lcm = lcm(*balls)
        for ball_candidate in divisors(target)[1::]:
            if ball_candidate not in balls and lcm(ball_candidate,balls_lcm) == target:
                print(ball_candidate)
                break
        else:
            print('impossivel')
