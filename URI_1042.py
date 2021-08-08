list_input = list(map(int, input().split()))
list_sorted = list_input.copy()
list_sorted.sort()

for element in list_sorted:
    print(element)
print()
for element in list_input:
    print(element)