while True:
    try:
        string = input()
    except EOFError:
        break

    substrings = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.add(string[i:j])
    print('\n'.join(sorted(substrings)))
    print()
