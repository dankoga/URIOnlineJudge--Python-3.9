tests_qty = int(input())
for t in range(tests_qty):
    bottles, exchange_number = map(int, input().split())
    print(sum(divmod(bottles, exchange_number)))
