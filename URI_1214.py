tests_qty = int(input())
for t in range(tests_qty):
    students_qty, *grades = map(float, input().split())
    grade_avg = sum(grades) / students_qty
    above_avg_qty = sum([float(g > grade_avg) for g in grades])
    print('{:.3f}%'.format(above_avg_qty / students_qty * 100.0))
