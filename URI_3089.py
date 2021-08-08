from operator import add

children_qty = int(input())
while children_qty > 0:
    gift_prices = list(map(int, input().split()))
    pair_prices = list(map(add, gift_prices[:children_qty], gift_prices[:(children_qty - 1):-1]))
    print('{} {}'.format(max(pair_prices), min(pair_prices)))
    children_qty = int(input())
