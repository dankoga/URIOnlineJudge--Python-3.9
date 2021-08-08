tests_qty = int(input())
for t in range(tests_qty):
    text = ''.join(input().replace(',', '').split())
    letters_present = [0 for i in range(26)]
    for c in text:
        letters_present[ord(c) - 97] = 1
    letters_distinct = sum(letters_present)
    if letters_distinct == 26:
        print('frase completa')
    elif letters_distinct >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
