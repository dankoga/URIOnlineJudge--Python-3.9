tests_qty = int(input())
for t in range(tests_qty):
    factor_A, factor_B = map(int, input().split('x'))
    if factor_A == factor_B:
        for f in range(5, 11):
            print('{} x {} = {}'.format(factor_A, f, factor_A * f))
    else:
        for f in range(5,11):
            print('{} x {} = {} && {} x {} = {}'.format(factor_A, f, factor_A * f, factor_B, f, factor_B * f))
