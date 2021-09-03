if __name__ == '__main__':
    while True:
        sentence = input().split()
        if sentence[0] == '*':
            break
        repeating_letter = sentence[0][0].upper()
        for word in sentence[1:]:
            if word[0].upper() != repeating_letter:
                print('N')
                break
        else:
            print('Y')
