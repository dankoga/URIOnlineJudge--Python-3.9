while True:
    try:
        people_qty, meetings_qty = map(int, input().split())
    except EOFError:
        break

    date_found = False
    for date in range(meetings_qty):
        if date_found:
            input()
        else:
            input_line = input().split()
            people = list(map(int, input_line[1:]))
            if sum(people) == people_qty:
                date_found = True
                print(input_line[0])
    if not date_found:
        print('Pizza antes de FdI')
