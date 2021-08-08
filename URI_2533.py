while True:
    try:
        subjects_qty = int(input())
    except EOFError:
        break
    grades_total = 0
    workload_total = 0
    for subject in range(subjects_qty):
        grade, workload = map(float, input().split())
        grades_total += grade * workload
        workload_total += workload
    print('{:.4f}'.format(grades_total / (100.0 * workload_total)))
