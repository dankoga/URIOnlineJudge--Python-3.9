def string_to_binary(string):
    return sum([int(c == 'O') * 2 ** i for i, c in enumerate(string)])


def binary_to_string(number):
    return '{:b}'.format(number).replace('0', 'X').replace('1', 'O')


tests_qty = int(input())
for t in range(tests_qty):
    lights, changes_qty = input().split()
    lights_new = binary_to_string(string_to_binary(lights) + int(changes_qty))[::-1]
    print(('{:X<' + str(len(lights)) + '}').format(lights_new[:len(lights)]))
