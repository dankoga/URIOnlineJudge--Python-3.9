submissions_qty = int(input())
while submissions_qty > 0:
    status_table = [0 for p in range(26)]
    time_table = [0 for p in range(26)]
    for s in range(submissions_qty):
        problem, time, status = input().split()
        if status == 'correct':
            status_table[ord(problem) - 65] = 1
            time_table[ord(problem) - 65] += int(time)
        else:
            time_table[ord(problem) - 65] += 20
    correct_count = sum(status_table)
    total_time = sum([time_table[p] * status_table[p] for p in range(26)])
    print('{} {}'.format(correct_count, total_time))
    submissions_qty = int(input())
