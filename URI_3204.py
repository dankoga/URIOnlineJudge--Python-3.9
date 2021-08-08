hex_sequence = [1, 0, 6]
for n in range(3, 15):
    h = (36 * (n - 2) * (n - 1) * hex_sequence[n - 3] +
         24 * (n - 1) * (n - 1) * hex_sequence[n - 2] +
                    n * (n - 1) * hex_sequence[n - 1]) // (n ** 2)
    hex_sequence.append(h)

tests_qty = int(input())
for t in range(tests_qty):
    print(hex_sequence[int(input())])
