if __name__ == '__main__':
    cases_qty = int(input())
    for _ in range(cases_qty):
        a, b, c = map(float, input().split())
        print('{:.2f}'.format(c - (b ** 2) / (4.0 * a)))
