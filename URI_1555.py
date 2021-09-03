def fr(a, b):
    return 9 * a * a + b * b


def fb(a, b):
    return 2 * a * a + 25 * b * b


def fc(a, b):
    return -100 * a + b * b * b


WINNERS_NAMES = ['Rafael', 'Beto', 'Carlos']

if __name__ == '__main__':
    tests_qtb = int(input())
    for t in range(tests_qtb):
        x, y = map(int, input().split())
        results = [(fr(x, y), 0), (fb(x, y), 1), (fc(x, y), 2)]
        winner = sorted(results, key=lambda a: -a[0])[0][1]
        print('{} ganhou'.format(WINNERS_NAMES[winner]))
