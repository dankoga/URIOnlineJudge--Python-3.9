NOTES = [100,
         50,
         20,
         10,
         5,
         2]
COINS = [100,
         50,
         25,
         10,
         5,
         1]


value_ints, value_cents = map(int, input().split('.'))

print("NOTAS:")
for note in NOTES:
    note_qty, value_ints = divmod(value_ints, note)
    print("{} nota(s) de R$ {}.00".format(note_qty, note))
value_cents += 100 * value_ints

print("MOEDAS:")
for coin in COINS:
    coin_qty, value_cents = divmod(value_cents, coin)
    print("{} moeda(s) de R$ {:0.2f}".format(coin_qty, coin/100))
