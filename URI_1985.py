MENU = {1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50}

items_qty = int(input())
purchase_total = 0.0
for item in range(items_qty):
    product_code, product_qty = map(int, input().split())
    purchase_total += MENU[product_code] * product_qty
print('{:.2f}'.format(purchase_total))
