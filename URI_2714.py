students_qty = int(input())
for s in range(students_qty):
    record_code = input()
    if len(record_code) != 20 or record_code[:2] != 'RA':
        print('INVALID DATA')
    else:
        print(record_code[2:].lstrip('0'))
