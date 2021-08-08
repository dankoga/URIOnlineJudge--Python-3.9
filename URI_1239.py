import re


def italic(m):
    return '<i>' + m.group(2) + '</i>'


def bold(m):
    return '<b>' + m.group(2) + '</b>'


while True:
    try:
        text = input()
    except EOFError:
        break
    print(re.sub(r"(\*)(.*?)(\*)", bold, re.sub(r"(_)(.*?)(_)", italic, text)))
