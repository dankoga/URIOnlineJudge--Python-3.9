from math import log10

POW10 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]


def count_from_1(n):
    count = [0] * 10
    if n == 0:
        return count

    power_max = int(log10(n))
    for p, d in enumerate([int(i) for i in str(n)]):
        left_side, right_side = divmod(n, POW10[power_max - p])
        count[d] += right_side + 1
        left_side //= 10

        for i in range(d):
            count[i] += (left_side + 1) * POW10[power_max - p]
        for i in range(d, 10):
            count[i] += left_side * POW10[power_max - p]

        count[0] -= POW10[power_max - p]
    return count


if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        digits_count_a = count_from_1(a - 1)
        digits_count_b = count_from_1(b)
        digit_count_from_a_to_b = [digits_count_b[i] - digits_count_a[i] for i in range(10)]
        print(' '.join([str(d) for d in digit_count_from_a_to_b]))
