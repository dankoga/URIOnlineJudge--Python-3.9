input_size = int(input())
for input_line in range(input_size):
    name, force = input().split()
    if name == 'Thor':
        print('Y')
    else:
        print('N')
