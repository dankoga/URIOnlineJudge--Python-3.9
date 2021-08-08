entries_qty = int(input())
entries_list = [list(input().split()) for e in range(entries_qty)]
entries_signed = [int(entry[1]) if entry[0] == 'V' else -1 * int(entry[1])
                  for entry in entries_list  ]
if sum(entries_signed) >= 0:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
