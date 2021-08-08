from sys import stdin

biggest_number = 0
biggest_index = 1
index = 1
for input_line in stdin:
    try:
        number = int(input_line)
    except:
        break
    if number > biggest_number:
        biggest_number = number
        biggest_index = index
    index += 1
print(biggest_number)
print(biggest_index)