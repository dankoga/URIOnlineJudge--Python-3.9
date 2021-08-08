def read_eyes(eyes_str):
    return 4 * (eyes_str[0] == '*') +  2 * (eyes_str[1] == '*') + (eyes_str[2] == '*')


for input_case in range(3):
    number = 0
    while True:
        input_line = input()
        if input_line == 'caw caw':
            break
        number += read_eyes(input_line)
    print(number)
