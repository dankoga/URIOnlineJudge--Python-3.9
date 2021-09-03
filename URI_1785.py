def kaprekar_cycle(n):
    count = 0
    while n != 6174:
        count += 1
        n_list = list('{:04d}'.format(n))
        n_list.sort(reverse=True)
        n_str = ''.join([str(d) for d in n_list])
        n = int(n_str) - int(n_str[::-1])
    return count


if __name__ == '__main__':
    for case_number in range(1, int(input()) + 1):
        seed = int(input())
        if seed % 1111 == 0:
            print('Caso #{}: -1'.format(case_number))
        else:
            print('Caso #{}: {}'.format(case_number, kaprekar_cycle(seed)))
