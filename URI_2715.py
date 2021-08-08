from itertools import accumulate


def binary_search(search_list, element):
    index_lower = 0
    index_upper = len(search_list) - 1
    while True:
        if index_upper - index_lower <= 1:
            return min([abs(2 * search_list[index_lower] - element), abs(2 * search_list[index_upper] - element)])
        index_middle = (index_lower + index_upper) // 2
        if 2 * search_list[index_middle] > element:
            index_upper = index_middle
        elif 2 * search_list[index_middle] < element:
            index_lower = index_middle
        else:
            return 0


while True:
    try:
        assignments_qty = int(input())
    except EOFError:
        break
    assignments = list(map(int, input().split()))
    assignments_total = sum(assignments)
    assignments_accumulative = list(accumulate(assignments))
    print(binary_search(assignments_accumulative, assignments_total))
