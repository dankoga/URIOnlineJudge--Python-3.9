import re

while True:
    try:
        tag = input().lower()
    except EOFError:
        break
    tag_replacement = input()
    text = input()

    text_replaced = []
    index_begin = 0
    index_end = 0
    regex = re.compile(tag, re.IGNORECASE)
    while index_end < len(text):
        while index_end < len(text) and text[index_end] != '<':
            index_end += 1
        text_replaced += text[index_begin:index_end]
        index_begin = index_end
        while index_end < len(text) and text[index_end] != '>':
            index_end += 1
        text_replaced += regex.sub(tag_replacement, text[index_begin:index_end])
        index_begin = index_end
    print(''.join(text_replaced))
