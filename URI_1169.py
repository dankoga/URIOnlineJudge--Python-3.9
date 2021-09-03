tests_qty = int(input())
for t in range(tests_qty):
    squares = int(input())
    print('{} kg'.format((2 ** squares) // 12000))
