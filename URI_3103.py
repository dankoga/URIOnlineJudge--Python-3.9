tests_qty = int(input())
for t in range(tests_qty):
    number = input().rstrip()

    digit_freq = [0 for d in range(10)]
    for d in number:
        digit_freq[int(d)] += 1

    smallest_nonzero = 1
    while digit_freq[smallest_nonzero] == 0:
        smallest_nonzero += 1
    digit_freq[smallest_nonzero] -= 1
    print(str(smallest_nonzero) + ''.join([str(i) * digit_freq[i] for i in range(0, 10)]))
