tests_qty = int(input())
for t in range(tests_qty):
    string_a, string_b = input().split()

    if len(string_a) > len(string_b):
        print(''.join(s[0] + s[1] for s in list(zip(string_a, string_b))) + string_a[len(string_b):])
    else:
        print(''.join(s[0] + s[1] for s in list(zip(string_a, string_b))) + string_b[len(string_a):])
