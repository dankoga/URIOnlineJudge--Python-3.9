cards_total = int(input())
cards_bought = int(input())
cards_collected = set()
for c in range(cards_bought):
    card = input()
    if not(card in cards_collected):
        cards_collected.add(card)
print(cards_total - len(cards_collected))
