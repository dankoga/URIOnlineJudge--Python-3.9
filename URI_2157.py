tests_qty = int(input())
for t in range(tests_qty):
    begin, end = map(int, input().split())
    sequence_str = ''.join([str(n) for n in range(begin, end + 1)])
    print(sequence_str + sequence_str[::-1])
