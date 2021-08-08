cases_qty = int(input())
for c in range(cases_qty):
    a_strings = input().replace('h', ' ').replace('k', ' ').replace('m', ' ').replace('e', ' ').split()
    print('k' + 'a' * (len(a_strings[0]) * len(a_strings[1])))
