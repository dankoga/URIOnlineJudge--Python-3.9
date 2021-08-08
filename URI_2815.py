text = input().split()
for i in range(len(text)):
    if len(text[i]) >= 4:
        if text[i][:2] == text[i][2:4]:
            text[i] = text[i][2:]
print(' '.join(text))
