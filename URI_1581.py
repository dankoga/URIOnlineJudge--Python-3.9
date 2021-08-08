tests_qty = int(input())
for t in range(tests_qty):
    people_qty = int(input())
    languages = set()
    for p in range(people_qty):
        languages.add(input())
    if len(languages) > 1:
        print('ingles')
    else:
        print(*languages)
