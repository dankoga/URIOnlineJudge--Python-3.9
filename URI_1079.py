input_size = int(input())
for input_case in range(input_size):
    number_A, number_B, number_C = map(float, input().split())
    print('{:.1f}'.format((2.0 * number_A + 3.0 * number_B + 5.0 * number_C)/10.0))