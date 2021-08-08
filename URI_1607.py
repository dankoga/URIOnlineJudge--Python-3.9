tests_qty = int(input())
for t in range(tests_qty):
    text_a, text_b = input().split()
    print(sum([(ord(text_b[i]) - ord(text_a[i]) + 26) % 26 for i in range(len(text_a))]))
