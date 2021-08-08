price_old, price_new = map(float, input().split())
print('{:.2f}%'.format(100.0 * (price_new - price_old) / price_old))
