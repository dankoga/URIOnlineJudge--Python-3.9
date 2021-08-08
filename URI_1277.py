tests_qty = int(input())
for t in range(tests_qty):
    students_qty = input()
    students_names = list(input().split())
    students_attendance = list(input().split())
    students_failed = []
    for s, attendance in enumerate(students_attendance):
        presences = attendance.count('P')
        medicals = attendance.count('M')
        if 4 * presences < 3 * (len(attendance) - medicals):
            students_failed += [students_names[s]]
    print(' '.join([student for student in students_failed]))
