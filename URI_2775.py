def merge_sort(tuple_list):
    total_time = 0
    sublist_size = 1
    while sublist_size < len(tuple_list):
        l_begin = 0
        while l_begin < len(tuple_list):
            l = l_begin
            l_end = min(l + sublist_size, len(tuple_list))
            r = l_end
            r_end = min(r + sublist_size, len(tuple_list))

            temp_list = []
            while l < l_end and r < r_end:
                if tuple_list[l][0] < tuple_list[r][0]:
                    temp_list.append(tuple_list[l])
                    l += 1
                else:
                    temp_list.append(tuple_list[r])
                    times = [t[1] for t in tuple_list[l:l_end]]
                    total_time += sum(times) + len(times) * tuple_list[r][1]
                    r += 1
            temp_list += tuple_list[l:l_end]
            temp_list += tuple_list[r:r_end]
            tuple_list[l_begin:r_end] = temp_list
            l_begin += 2 * sublist_size
        sublist_size *= 2
    return total_time


while True:
    try:
        packet_qty = int(input())
    except EOFError:
        break

    packets_id = list(map(int, input().split()))
    packets_time = list(map(int, input().split()))
    packets_sort = list(zip(packets_id, packets_time))
    print(merge_sort(packets_sort))
