while True:
    try:
        attributes_qty = int(input())
    except EOFError:
        break

    player1_deck_size, player2_deck_size = map(int, input().split())
    player1_deck = []
    for card in range(player1_deck_size):
        player1_deck.append((list(map(int, input().split()))))
    player2_deck = []
    for card in range(player2_deck_size):
        player2_deck.append((list(map(int, input().split()))))

    player1_card, player2_card = map(int, input().split())
    attribute = int(input()) - 1
    if player1_deck[player1_card - 1][attribute] > player2_deck[player2_card - 1][attribute]:
        print('Marcos')
    elif player1_deck[player1_card - 1][attribute] < player2_deck[player2_card - 1][attribute]:
        print('Leonardo')
    else:
        print('Empate')
