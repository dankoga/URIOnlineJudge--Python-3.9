lists_qty = int(input())
for ls in range(lists_qty):
    list_size = int(input())
    numbers_list = list(map(int, input().split()))
    odd_list = [number for number in numbers_list if (number % 2 == 1)]
    odd_list.sort()
    index_head = 0
    index_tail = len(odd_list) - 1
    output_list = []
    while index_head < index_tail:
        output_list.append(str(odd_list[index_tail]))
        output_list.append(str(odd_list[index_head]))
        index_head += 1
        index_tail -= 1
    if index_head == index_tail:
        output_list.append(str(odd_list[index_tail]))
    print(' '.join(output_list))
