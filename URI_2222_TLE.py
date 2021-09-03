from functools import reduce


def count_ones(n):
    # Using Brian Kernighan’s algorithm
    counter = 0
    while n > 0:
        n &= n - 1
        counter += 1
    return counter


if __name__ == '__main__':
    instances_qty = int(input())
    for i in range(instances_qty):
        sets_qty = int(input())
        binary_coded_sets_list = []
        for s in range(sets_qty):
            binary_coded_elements = [2 ** int(e) for e in input().split()[1:]]
            binary_coded_sets_list.append(reduce(lambda x, y: x | y, binary_coded_elements))

        operations_qty = int(input())
        for o in range(operations_qty):
            op, s1, s2 = map(int, input().split())
            if op == 1:
                print(count_ones(binary_coded_sets_list[s1 - 1] & binary_coded_sets_list[s2 - 1]))
            else:
                print(count_ones(binary_coded_sets_list[s1 - 1] | binary_coded_sets_list[s2 - 1]))
