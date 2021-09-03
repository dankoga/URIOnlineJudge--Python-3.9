while True:
    try:
        new_students_qty, year = input().split()
    except EOFError:
        break
    usernames_set = set()
    non_standard_username_qty = 0
    for s in range(int(new_students_qty)):
        new_username = ''.join([name[0] for name in input().split()])
        usernames_set.add(new_username)
    print(int(new_students_qty) - len(usernames_set))
