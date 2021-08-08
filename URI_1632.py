import math


VARIATIONS = [3, 2, 2, 2, 3, 2,
              2, 2, 3, 2, 2, 2,
              2, 2, 3, 2, 2, 2,
              3, 2, 2, 2, 2, 2,
              2, 2]


tests_qty = int(input())
for t in range(tests_qty):
    password = input().lower()
    print(math.prod([VARIATIONS[ord(c) - 97] for c in password]))
