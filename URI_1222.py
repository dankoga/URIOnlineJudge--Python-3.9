from math import ceil


while True:
    try:
        word_count, lines_per_page, chars_per_line = map(int, input().split())
    except EOFError:
        break
    story_string = input()
    index_begin = 0
    lines_total = 1
    while index_begin + chars_per_line < len(story_string):
        if story_string[index_begin + chars_per_line - 1] == ' ':
            index_begin += chars_per_line
        else:
            if story_string[index_begin + chars_per_line] == ' ':
                index_begin += + chars_per_line + 1
            else:
                index_begin = story_string.rfind(' ', 0, index_begin + chars_per_line) + 1
        lines_total += 1
    print(ceil(lines_total / lines_per_page))
