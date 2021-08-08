number_binary = input()
ones_qty = number_binary.count('1')
parity_bit = str(ones_qty % 2)
print(number_binary + parity_bit)
