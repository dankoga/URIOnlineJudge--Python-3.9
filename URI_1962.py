input_size = int(input())
for input_line in range(input_size):
    years_ago = int(input())
    year = 2015 - years_ago
    if year > 0:
        print('{} D.C.'.format(year))
    else:
        print('{} A.C.'.format(abs(year) + 1))
