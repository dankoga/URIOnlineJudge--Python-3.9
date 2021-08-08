column_to_process = int(input())
operation = input()
column_sum = 0
for line_index in range(12):
    for column_index in range(12):
        if column_index == column_to_process:
            column_sum += float(input())
        else:
            input()
if operation == 'S':
    print('{:.1f}'.format(column_sum))
else:
    print('{:.1f}'.format(column_sum/12.0))
