def is_dangerous(string_base, string_danger):
    found_index = string_base.find(string_danger)
    next_index = found_index + len(string_danger)
    return found_index != -1 and \
           (next_index == len(string_base) or string_base[next_index].isupper())


tests_qty = int(input())
for test in range(tests_qty):
    if test != 0:
        print()
    molecules_dangerous_qty = int(input())
    molecules_dangerous_list = [input() for molecule in range(molecules_dangerous_qty)]
    molecules_test_qty = int(input())
    for molecule in range(molecules_test_qty):
        molecule_test = input()
        for molecule_dangerous in molecules_dangerous_list:
            if is_dangerous(molecule_test, molecule_dangerous):
                print('Abortar')
                break
        else:
            print('Prossiga')
