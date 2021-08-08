children_qty = int(input())
for c in range(children_qty):
    string_a = input()
    string_b = input()
    name = ''.join([string_a[i:i + 2] + string_b[i:i + 2] for i in range(0, len(string_a), 2)])
    print(name)
