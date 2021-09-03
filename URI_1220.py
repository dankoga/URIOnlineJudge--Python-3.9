from math import ceil, floor

while True:
    students_qty = int(input())
    if students_qty == 0:
        break

    money_per_student = [float(input()) for s in range(students_qty)]
    money_avg = sum(money_per_student) / students_qty

    money_given = 0.0
    money_taken = 0.0
    for m in money_per_student:
        money_difference = m - money_avg
        if money_difference >= 0:
            money_given += floor(100.0 * money_difference) / 100.0
        else:
            money_taken -= ceil(100.0 * money_difference) / 100.0
    print('${:.2f}'.format(max(money_given, money_taken)))
