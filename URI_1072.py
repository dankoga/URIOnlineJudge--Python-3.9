input_size = int(input())
inside_qty = 0
for input_number in range(input_size):
    number = int(input())
    inside_qty += int(10 <= number <= 20)
print('{} in\n{} out'.format(inside_qty, input_size - inside_qty))
