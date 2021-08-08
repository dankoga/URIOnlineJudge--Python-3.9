students_qty = int(input())
students_list = []
for student in range(students_qty):
    student_input = input().split()
    students_list.append([student_input[0], float(student_input[1])])
students_list.sort(key=(lambda x: x[1]), reverse=True)
if students_list[0][1] >= 8.0:
    print(students_list[0][0])
else:
    print('Minimum note not reached')
