NOTES = [100,
         50,
         20,
         10,
         5,
         2,
         1]

value = int(input())

print(value)
for note in NOTES:
    note_qty, value = divmod(value, note)
    print("{} nota(s) de R$ {},00".format(note_qty, note))
