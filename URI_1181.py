line_to_process = int(input())
operation = input()
line_sum = 0
for line_index in range(12):
    if line_index == line_to_process:
        for column_index in range(12):
            line_sum += float(input())
    else:
        for column_index in range(12):
            input()
if operation == 'S':
    print('{:.1f}'.format(line_sum))
else:
    print('{:.1f}'.format(line_sum/12.0))