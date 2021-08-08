import re

tests_qty = int(input())
numbers_pattern = re.compile('[0-9]+')
for t in range(tests_qty):
    numbers_list = re.findall(numbers_pattern, input())
    print(sum([int(n) for n in numbers_list]))
