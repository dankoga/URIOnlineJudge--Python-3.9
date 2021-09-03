tests_qty = int(input())
for t in range(tests_qty):
    uses_qty = int(input())
    possessions = set()
    for u in range(uses_qty):
        thing, incantation = input().split()
        if incantation == 'chirrin':
            possessions.add(thing)
        elif incantation == 'chirrion' and thing in possessions:
            possessions.remove(thing)
    print('TOTAL')
    print('\n'.join([thing for thing in sorted(possessions)]))
