import sys

input_file = sys.stdin.readlines()

line = 0
while '<body>' not in input_file[line]:
    line += 1
line += 1
while '</body>' not in input_file[line]:
    print(input_file[line], end='')
    line += 1
