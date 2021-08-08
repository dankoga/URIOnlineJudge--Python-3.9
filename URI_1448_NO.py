import sys


sys.stdin.reconfigure(errors='ignore')


instances_qty = int(input())
for instance in range(1, instances_qty + 1):
    original_message = input()
    team_1_message = input()
    team_2_message = input()

    length_max = max([len(original_message), len(team_1_message), len(team_2_message)])
    reformat_string = '{:<' + str(length_max) + '}'
    original_message = reformat_string.format(original_message)
    team_1_message = reformat_string.format(team_1_message)
    team_2_message = reformat_string.format(team_2_message)

    team_1_score = team_2_score = 0
    first_right = 0
    for index, character in enumerate(original_message):
        team_1_right = team_1_message[index] == character
        team_2_right = team_2_message[index] == character
        team_1_score += int(team_1_right)
        team_2_score += int(team_2_right)
        if not first_right:
            if team_1_right and not team_2_right:
                first_right = 1
            if team_2_right and not team_1_right:
                first_right = 2
    print('Instancia {}'.format(instance))
    if team_1_score > team_2_score:
        print('time 1')
    elif team_2_score > team_1_score:
        print('time 2')
    else:
        if first_right == 1:
            print('time 1')
        elif first_right == 2:
            print('time 2')
        else:
            print('empate')
    print()
