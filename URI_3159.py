KEYS = {'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        'A': '#2', 'B': '#22', 'C': '#222',
        'D': '#3', 'E': '#33', 'F': '#333',
        'G': '#4', 'H': '#44', 'I': '#444',
        'J': '#5', 'K': '#55', 'L': '#555',
        'M': '#6', 'N': '#66', 'O': '#666',
        'P': '#7', 'Q': '#77', 'R': '#777', 'S': '#7777',
        'T': '#8', 'U': '#88', 'V': '#888',
        'W': '#9', 'X': '#99', 'Y': '#999', 'Z': '#9999',
        ' ': '0'}

SAME_KEYS = {'a' : 'abc', 'b': 'abc', 'c': 'abc',
             'd' : 'def', 'e': 'def', 'f': 'def',
             'g' : 'ghi', 'h': 'ghi', 'i': 'ghi',
             'j' : 'jkl', 'k': 'jkl', 'l': 'jkl',
             'm' : 'mno', 'n': 'mno', 'o': 'mno',
             'p' : 'pqrs', 'q': 'pqrs', 'r': 'pqrs', 's': 'pqrs',
             't' : 'tuv', 'u': 'tuv', 'v': 'tuv',
             'w' : 'wxyz', 'x': 'wxyz', 'y': 'wxyz', 'z': 'wxyz'}

tests_qty = int(input())
for t in range(tests_qty):
    word = input()
    keys = [KEYS[word[0]]]
    for i in range(1, len(word)):
        if word[i].isalpha() and word[i - 1].lower() in SAME_KEYS[word[i].lower()] and word[i].islower():
            keys += ['*' + KEYS[word[i]]]
        else:
            keys += [KEYS[word[i]]]
    print(''.join(keys))
