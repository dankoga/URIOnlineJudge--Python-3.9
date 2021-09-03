import sys

line_width = int(input())
text = [lines.rstrip() for lines in sys.stdin if len(lines.rstrip()) > 0]
line_count = 0
for line in text:
    index = line_width
    line_count += 1
    while index < len(line):
        while index < len(line) and line[index].isspace():
            index += 1
        index += line_width
        line_count += 1
print(line_count)
