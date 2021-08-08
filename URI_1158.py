input_size = int(input())
for input_line in range(input_size):
    a1, n = map(int, input().split())
    a1 += 1 - a1 % 2
    print('{}'.format(n * (a1 + n - 1)))
