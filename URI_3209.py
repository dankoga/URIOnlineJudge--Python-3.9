tests_qty = int(input())
for t in range(tests_qty):
    strips = list(map(int, input().split()))
    print(sum(strips[1:]) - strips[0] + 1)
