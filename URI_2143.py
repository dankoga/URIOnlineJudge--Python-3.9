cases_qty = int(input())
while cases_qty > 0:
    for case in range(cases_qty):
        people_qty = int(input())
        print(2 * people_qty - 2 + people_qty % 2)
    cases_qty = int(input())
