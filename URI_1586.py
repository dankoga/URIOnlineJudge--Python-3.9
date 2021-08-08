import sys


def binary_search(search_list):
    begin = 0
    end = len(search_list)
    pivot = end // 2
    while begin != end - 1:
        strength_L = sum([s * i for i, s in enumerate(search_list[pivot::-1], start=1)])
        strength_R = sum([s * i for i, s in enumerate(search_list[pivot + 1:], start=1)])
        if strength_L > strength_R:
            end = pivot
            pivot = (pivot + begin) // 2
        elif strength_L < strength_R:
            begin = pivot
            pivot = (end + pivot) // 2
        else:
            return pivot
    strength_L = sum([s * i for i, s in enumerate(search_list[begin::-1], start=1)])
    strength_R = sum([s * i for i, s in enumerate(search_list[begin + 1:], start=1)])
    if strength_L == strength_R:
        return begin
    strength_L = sum([s * i for i, s in enumerate(search_list[end::-1], start=1)])
    strength_R = sum([s * i for i, s in enumerate(search_list[end + 1:], start=1)])
    if strength_L == strength_R:
        return end
    return -1


input_file = sys.stdin.readlines()
file_counter = 0
while True:
    students_qty = int(input_file[file_counter])
    file_counter += 1
    if students_qty == 0:
        break

    students_name = [name.strip() for name in input_file[file_counter:(file_counter + students_qty)]]
    file_counter += students_qty
    students_self_strength = [sum([ord(c) for c in name]) for name in students_name]

    student_half = binary_search(students_self_strength)
    if student_half < 0:
        print('Impossibilidade de empate.')
    else:
        print(students_name[student_half])
