def josephus(n, k):
    r = 0
    for i in range(1, n + 1):
        r = (r + k) % i
    return r + 1


if __name__ == '__main__':
    for c in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        print('Case {}: {}'.format(c, josephus(n, k)))
