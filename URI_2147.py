cases_qty = int(input())
for case in range(cases_qty):
    word = input()
    print('{:.2f}'.format(len(word)/100.0))
