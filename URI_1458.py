import math


letter_time = [0.2, 0.4, 0.6,
               0.2, 0.4, 0.6,
               0.2, 0.4, 0.6,
               0.2, 0.4, 0.6,
               0.2, 0.4, 0.6,
               0.2, 0.4, 0.6, 0.8,
               0.2, 0.4, 0.6,
               0.2, 0.4, 0.6, 0.8,
               0.2]

para_01 = 1.0/30.0
para_02 = 1.0/15.0
para_03 = 0.1
diag_11 = math.hypot(1, 1)/30.0
diag_12 = math.hypot(1, 2)/30.0
diag_13 = math.hypot(1, 3)/30.0
letter_interval = 3 * [3 * [2.0 * diag_13] +
                       3 * [para_01] +
                       3 * [diag_11] +
                       3 * [para_01] +
                       3 * [diag_11] +
                       4 * [diag_12] +
                       3 * [para_02] +
                       4 * [diag_12] +
                       [para_03]]
letter_interval += 3 * [3 * [para_01] +
                        3 * [2.0 * para_03] +
                        3 * [diag_12] +
                        3 * [diag_11] +
                        3 * [para_01] +
                        4 * [2.0 * diag_11] +
                        3 * [diag_12] +
                        4 * [para_02] +
                        [diag_13]]
letter_interval += 3 * [3 * [diag_11] +
                        3 * [diag_12] +
                        3 * [4.0 * diag_11] +
                        3 * [para_01] +
                        3 * [para_02] +
                        4 * [para_01] +
                        3 * [diag_11] +
                        4 * [diag_12] +
                        [diag_12]]
letter_interval += 3 * [3 * [para_01] +
                        3 * [diag_11] +
                        3 * [para_01] +
                        3 * [2.0 * diag_12] +
                        3 * [para_01] +
                        4 * [diag_11] +
                        3 * [para_01] +
                        4 * [diag_11] +
                        [para_02]]
letter_interval += 3 * [3 * [diag_11] +
                        3 * [para_01] +
                        3 * [para_02] +
                        3 * [para_01] +
                        3 * [2.0 * para_02] +
                        4 * [diag_12] +
                        3 * [diag_11] +
                        4 * [para_01] +
                        [diag_12]]
letter_interval += 4 * [3 * [diag_12] +
                        3 * [2.0 * diag_11] +
                        3 * [para_01] +
                        3 * [diag_11] +
                        3 * [diag_12] +
                        4 * [2.0 * diag_12] +
                        3 * [para_01] +
                        4 * [para_02] +
                        [diag_11]]
letter_interval += 3 * [3 * [para_02] +
                        3 * [diag_12] +
                        3 * [diag_11] +
                        3 * [para_01] +
                        3 * [diag_11] +
                        4 * [para_01] +
                        3 * [2.0 * diag_11] +
                        4 * [para_01] +
                        [para_01]]
letter_interval += 4 * [3 * [diag_12] +
                        3 * [para_02] +
                        3 * [diag_12] +
                        3 * [diag_11] +
                        3 * [para_01] +
                        4 * [para_02] +
                        3 * [para_01] +
                        4 * [2.0 * para_01] +
                        [diag_11]]
letter_interval += 1 * [3 * [para_03] +
                        3 * [diag_13] +
                        3 * [diag_12] +
                        3 * [para_02] +
                        3 * [diag_12] +
                        4 * [diag_11] +
                        3 * [para_01] +
                        4 * [diag_11] +
                        [para_01]]

number_to_letter = ['{', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

letter_to_number = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7 ,7, 8, 8, 8, 9, 9, 9, 9, 0]


while True:
    try:
        text = input()
    except EOFError:
        break
    text = text.replace(' ', '{')
    time = sum([letter_time[ord(letter) - 97] for letter in text])

    thumb_R = 'mno'
    thumb_L = 'ghi'
    if not (text[0] in thumb_R + thumb_L):
        time_L = letter_interval[ord(text[0]) - 97][ord(thumb_R[0]) - 97]
        time_R = letter_interval[ord(text[0]) - 97][ord(thumb_R[0]) - 97]


    for letter in text:
        time_L = letter_interval[ord(letter) - 97][ord(thumb_L[0]) - 97]


