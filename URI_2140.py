POSSIBLE_VALUES = {4, 7, 10, 12, 15, 20, 22, 25, 30, 40, 52, 55, 60, 70,
                   100, 102, 105, 110, 120, 150, 200}

product_price, customer_paid = map(int, input().split())
while product_price * customer_paid != 0:
    change = customer_paid - product_price
    if change in POSSIBLE_VALUES:
        print('possible')
    else:
        print('impossible')
    product_price, customer_paid = map(int, input().split())
