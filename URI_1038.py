PRICE_TABLE = [4.00,
               4.50,
               5.00,
               2.00,
               1.50]

product_ID, product_qty = map(int, input().split())
print("Total: R$ {:.2f}".format(product_qty * PRICE_TABLE[product_ID - 1]))