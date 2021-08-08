while True:
    try:
        string_A = input()
    except EOFError:
        break
    string_B = input()

    if len(string_A) < len(string_B):
        search_string = string_A
        searched_string = string_B
    else:
        search_string = string_B
        searched_string = string_A

    for length_substring in range(len(search_string), 0, -1):
        for index_begin in range(0, len(search_string) - length_substring + 1):
            if search_string[index_begin:(index_begin + length_substring)] in searched_string:
                print(length_substring)
                break
        else:
            continue
        break
    else:
        print(0)
