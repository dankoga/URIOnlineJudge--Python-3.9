import sys

battles_qty = input()
battles_won = 0
for attacks in sys.stdin.readlines():
    if 'CD' not in attacks:
        battles_won += 1
print(battles_won)
