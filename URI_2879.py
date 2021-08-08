import sys

PRIZE = {'1\n': 0, '2\n': 1, '3\n': 1}

games_qty = input()
games_results = [PRIZE[door] for door in sys.stdin.readlines()]
print(sum(games_results))
