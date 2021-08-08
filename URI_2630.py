def mean(rgb):
    return sum(rgb) // 3


def eye(rgb):
    return (30 * rgb[0] + 59 * rgb[1] + 11 * rgb[2]) // 100


cases_qty = int(input())
for case in range(1, cases_qty + 1):
    method = input()
    rgb_color = list(map(int, input().split()))
    print('Caso #{}: {}'.format(case, eval(method + '(rgb_color)')))
