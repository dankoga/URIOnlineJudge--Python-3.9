input_size = int(input())
for input_line in range(input_size):
    dividend, divisor = map(float, input().split())
    if divisor == 0.0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(dividend/divisor))
