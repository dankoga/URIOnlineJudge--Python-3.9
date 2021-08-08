rows_qty = int(input())
cols_qty = int(input())
print(1 - (rows_qty & 1) ^ (cols_qty & 1) )
