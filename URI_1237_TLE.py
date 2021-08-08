while True:
    try:
        string_A = input()
    except EOFError:
        break
    string_B = input()

    len_A = len(string_A)
    len_B = len(string_B)
    comparison_matrix = [[int(letter_A == string_B[0]) for letter_A in string_A]]
    for index_B in range(1, len_B):
        comparison_matrix += [[int(string_A[0] == string_B[index_B])]]
        comparison_matrix[index_B] += [(comparison_matrix[index_B - 1][index_A - 1] + 1) *
                                       int(string_A[index_A] == string_B[index_B])
                                       for index_A in range(1, len_A)]

    print(max(max(comparison_matrix, key=max)))
