import sys


for line in sys.stdin:
    letter_visited = [False for letter in range(26)]
    for letter in ''.join(line.split()):
        letter_visited[ord(letter) - 97] = True

    letter_visited_str = ''.join([chr(n + 97) if visited else ' ' for n, visited in enumerate(letter_visited)])
    intervals_list = list(letter_visited_str.split())
    if len(intervals_list) == 0:
        print()
    else:
        print('{}:{}'.format(intervals_list[0][0], intervals_list[0][-1]), end='')
        for interval in intervals_list[1:]:
            print(', {}:{}'.format(interval[0], interval[-1]), end='')
        print()
