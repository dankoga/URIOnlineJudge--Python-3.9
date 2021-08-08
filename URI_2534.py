while True:
    try:
        entries_qty, queries_qty = map(int, input().split())
    except EOFError:
        break

    grades = []
    for entry in range(entries_qty):
        grades.append(int(input()))
    grades.sort(reverse=True)

    for query in range(queries_qty):
        print(grades[int(input()) - 1])
