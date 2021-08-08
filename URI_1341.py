import sys


DIRECTIONS = {'N': (-1, 0),
              'S': (1, 0),
              'E': (0, 1),
              'W': (0, -1)}


input_file = sys.stdin.readlines()
input_file = [line.rstrip() for line in input_file if line.strip()]
file_counter = 0

tests_qty = int(input_file[file_counter])
file_counter += 1
for t in range(1, tests_qty + 1):
    rows, cols = map(int, input_file[file_counter].split())
    file_counter += 1
    field = input_file[file_counter:file_counter + rows]
    file_counter += rows

    seq1_length, seq1_x, seq1_y = map(int, input_file[file_counter].split())
    file_counter += 1
    seq1_length += 1
    seq1_x -= 1
    seq1_y -= 1
    seq1 = [field[seq1_x][seq1_y]]
    if seq1_length > 1:
        for d in input_file[file_counter]:
            direction = DIRECTIONS[d]
            seq1_x += direction[0]
            seq1_y += direction[1]
            seq1 += [field[seq1_x][seq1_y]]
        file_counter += 1

    seq2_length, seq2_x, seq2_y = map(int, input_file[file_counter].split())
    file_counter += 1
    seq2_length += 1
    seq2_x -= 1
    seq2_y -= 1
    seq2 = [field[seq2_x][seq2_y]]
    if seq2_length > 1:
        for d in input_file[file_counter]:
            direction = DIRECTIONS[d]
            seq2_x += direction[0]
            seq2_y += direction[1]
            seq2 += [field[seq2_x][seq2_y]]
        file_counter += 1

    LCSmatrix = [[0 for s1 in range(seq1_length + 1)] for s2 in range(seq2_length + 1)]
    for s2 in range(1, seq2_length + 1):
        for s1 in range(1, seq1_length + 1):
            if seq1[s1 - 1] == seq2[s2 - 1]:
                LCSmatrix[s2][s1] = LCSmatrix[s2 - 1][s1 - 1] + 1
            else:
                LCSmatrix[s2][s1] = max(LCSmatrix[s2][s1 - 1], LCSmatrix[s2 - 1][s1])
    longest = LCSmatrix[-1][-1]
    print('Case {}: {} {}'.format(t, seq1_length - longest, seq2_length - longest))
