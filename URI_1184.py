operation = input()
cell_sum = 0.0
for line_index in range(12):
    for column_index in range(12):
        if column_index < line_index:
            cell_sum += float(input())
        else:
            input()
if operation == 'S':
    print('{:.1f}'.format(cell_sum))
else:
    print('{:.1f}'.format(cell_sum/66.0))
