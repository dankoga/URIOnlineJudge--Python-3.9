product = input().split()
product_qty = float(product[1])
product_price = float(product[2])

total = product_qty * product_price

product = input().split()
product_qty = float(product[1])
product_price = float(product[2])

total += product_qty * product_price

print("VALOR A PAGAR: R$ {:.2f}".format(total))
