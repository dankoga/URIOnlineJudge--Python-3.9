case_number = 1
while True:
    try:
        search_string = input()
        text_string = input()
    except EOFError:
        break
    print('Caso #{}:'.format(case_number))

    occurrence_index = text_string.find(search_string)
    if occurrence_index < 0:
        print('Nao existe subsequencia')
    else:
        occurrence_count = 0
        while occurrence_index >= 0:
            occurrence_index_old = occurrence_index
            occurrence_count += 1
            occurrence_index = text_string.find(search_string, occurrence_index_old + 1)
        print('Qtd.Subsequencias: {}'.format(occurrence_count))
        print('Pos: {}'.format(occurrence_index_old + 1))

    print()
    case_number += 1
