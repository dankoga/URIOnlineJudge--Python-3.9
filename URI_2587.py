def str_findall(pattern, string):
    index = string.find(pattern)
    while index != -1:
        yield index
        index = string.find(pattern, index +  1)

tests_qty = int(input())
for t in range(tests_qty):
    word_a = input()
    word_b = input()
    word_incomplete = input()
    idx = [i for i in str_findall('_', word_incomplete)]
    if word_a[idx[0]] == word_b[idx[1]] or word_a[idx[1]] == word_b[idx[0]]:
        print('Y')
    else:
        print('N')
