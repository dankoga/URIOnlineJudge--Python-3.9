import math

tests_qty = int(input())
for t in range(tests_qty):
    cards_A, cards_B = map(int, input().split())
    print(math.gcd(cards_A, cards_B))
